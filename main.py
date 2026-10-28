import json
import machine
import sys
import time

MENU_DIR = "/system/apps/menu"
APPS_DIR = "/system/apps"
MENU_MODULES = ("ui", "icons", "gallery", "app", "silhouettes", "achievements", "celebration", "opening", "mona3d", "mona")
preloaded = []


def intro_skipped():
    try:
        with open("/state/skip_intro.json") as f:
            return bool(json.load(f).get("on"))
    except (OSError, ValueError):
        return False


HOME_COMBO_MS = 1000
MENU_HOLD_MS = 400
combo_since = None
menu_since = None
home_since = None


def watch_home_combo(_timer):
    # leave any app by holding Left + Enter on the badge, or either middle pad button (MENU / HOME).
    # the Left + Enter and HOME pins are read directly, so those work even in an app that has stopped polling
    global combo_since, menu_since, home_since
    now = time.ticks_ms()
    if BUTTON_LEFT.value() or BUTTON_SELECT.value():
        combo_since = None
    elif combo_since is None:
        combo_since = now
    elif time.ticks_diff(now, combo_since) >= HOME_COMBO_MS:
        reset()
    if not badge.pad.held(BUTTON_MENU):
        menu_since = None
    elif menu_since is None:
        menu_since = now
    elif time.ticks_diff(now, menu_since) >= MENU_HOLD_MS:
        reset()
    if BUTTON_HOME.value() and not badge.pad.held(BUTTON_HOME):
        home_since = None
    elif home_since is None:
        home_since = now
    elif time.ticks_diff(now, home_since) >= MENU_HOLD_MS:
        reset()


try:
    import sparkle
except Exception as error:  # noqa: BLE001
    sparkle = None
    print("sparkle unavailable:", error)

if machine.reset_cause() != machine.WDT_RESET:
    badge.mode(HIRES | VSYNC)
    sys.path.insert(0, MENU_DIR)
    for name in MENU_MODULES:
        try:
            __import__(name)
            preloaded.append(name)
        except ImportError as error:
            print("menu preload failed:", name, error)
    try:
        sys.modules["app"].shared(APPS_DIR).preload_images()
        sys.modules["mona"].shared()
    except (KeyError, OSError) as error:
        print("menu preload failed:", error)
    sys.path.remove(MENU_DIR)
    if not intro_skipped():
        launch("/system/startup")

if sparkle is not None:
    try:
        sparkle.start(deferred=True)
    except Exception as error:  # noqa: BLE001
        print("sparkle unavailable:", error)

# Eat the wakeup button press to prevent it leaking into the menu
badge.poll()

# We expect a launcher menu to be at /system/apps/menu
app_to_launch = launch("/system/apps/menu")

for name in preloaded:
    sys.modules.pop(name, None)

# Stopping in Thonny can cause launch("/system/apps/menu") to return None
if app_to_launch is not None:

    # Don't pass menu button presses into the newly launched app
    while badge.pressed() or badge.held() or badge.released():
        badge.poll()

    try:
        home_timer = machine.Timer(period=50, mode=machine.Timer.PERIODIC, callback=watch_home_combo)
    except Exception as error:  # noqa: BLE001
        print("home combo unavailable:", error)

    launch(app_to_launch)

# Catch any exit and reset back to the launcher
reset()
