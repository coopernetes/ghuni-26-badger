import gc
import json

import ui
from app import BANNER_HEIGHT

AVATAR = 28
AVATAR_FILE = "/state/badge_avatar.png"
USER_FILE = "/state/badge_user.json"
RETRY_MS = 3000
RIGHT_LIMIT = 288


def load_handle():
    try:
        with open(USER_FILE) as f:
            login = json.load(f)["login"]
        gc.collect()
        return login
    except (OSError, ValueError, KeyError):
        pass
    try:
        import secrets
        return str(secrets.GITHUB_USERNAME).strip()
    except (ImportError, AttributeError):
        return ""


class Banner:
    def __init__(self):
        self.handle = load_handle()
        self.title = None
        self.avatar = None
        self.retry_at = 0
        self.count = (None, "", 0)

    def load_avatar(self):
        if self.avatar is not None or badge.ticks < self.retry_at:
            return
        self.retry_at = badge.ticks + RETRY_MS
        try:
            self.avatar = image.load(AVATAR_FILE)
        except Exception:  # noqa: BLE001
            pass

    def fit_title(self, x):
        text = "@" + self.handle if self.handle else ui.OS_NAME
        while len(text) > 1 and screen.measure_text(text)[0] > RIGHT_LIMIT - x:
            text = text[:-1]
        self.title = text

    def draw(self, apps, hidden=0.0):
        self.load_avatar()
        top = 3 - round(BANNER_HEIGHT * hidden)
        if self.avatar is not None:
            screen.blit(self.avatar, rect(ui.OS_X, top, AVATAR, AVATAR), image.BILINEAR)
        else:
            screen.pen = ui.shade(ui.PALETTE[0], 0.42)
            screen.rectangle(ui.OS_X, top, AVATAR, AVATAR)

        x = ui.OS_X + AVATAR + 8
        screen.font = ui.status_font
        if self.title is None:
            self.fit_title(x)
        screen.pen = ui.white
        screen.text(self.title, x, top)
        if self.handle:
            screen.pen = ui.dim_white
            screen.text(ui.OS_NAME, x, top + 15)

        ui.draw_battery(320 - ui.OS_X, top + 2)

        key = (apps.active_index, len(apps), apps.folder)
        if self.count[0] != key:
            text = f"{apps.active_index + 1:02d} / {len(apps):02d}"
            if apps.folder is not None:
                text = ui.lowercase(apps.folder.name) + "  " + text
            width, _ = screen.measure_text(text)
            self.count = (key, text, 320 - ui.OS_X - width)
        screen.pen = ui.dim_white
        screen.text(self.count[1], self.count[2], top + 15)
