# Runs on the badge via: mpremote connect /dev/ttyACM0 run docs/dump_help.py
import sys

MODULES = (
    "machine", "micropython", "gc", "os", "time", "json", "struct", "binascii", "random", "math", "array", "requests",
    "badgeware", "badgeware.ir", "badgeware.link", "wifi", "fetch", "missing_details", "powman", "sparkle",
    "hints", "pairing", "easing", "pico3d", "clock", "tufty",
)
GLOBALS = ("badge", "screen", "image", "shape", "color", "brush", "mat3", "font", "display", "rect", "run", "launch", "State")


def section(title, obj):
    print("\n@@@ " + title)
    try:
        help(obj)
    except Exception as error:  # noqa: BLE001
        print("help() failed:", error)
    try:
        print("@@@ dir:", " ".join(n for n in dir(obj) if not n.startswith("__")))
    except Exception as error:  # noqa: BLE001
        print("dir() failed:", error)


for name in MODULES:
    try:
        module = __import__(name)
        for part in name.split(".")[1:]:
            module = getattr(module, part)
    except Exception as error:  # noqa: BLE001
        print("\n@@@ " + name + " (unavailable: " + repr(error) + ")")
        continue
    section(name, module)

for name in GLOBALS:
    try:
        section("global: " + name, eval(name))
    except Exception as error:  # noqa: BLE001
        print("\n@@@ global: " + name + " (unavailable: " + repr(error) + ")")
