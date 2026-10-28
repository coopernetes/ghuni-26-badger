"""
Live machine stats: CPU, memory, flash and battery as percentages.

CPU is this app's share of each frame (time spent in update versus the frame
period), so it reads low on an idle screen. The clock speed is shown beside it.
"""

import gc
import machine
import os
import time

badge.mode(HIRES | VSYNC)
screen.antialias = image.X2

black = color.rgb(0, 0, 0)
white = color.rgb(255, 255, 255)
dim_white = color.rgb(255, 255, 255, 140)
track = color.rgb(255, 255, 255, 40)
good = color.rgb(95, 237, 131)
warn = color.rgb(255, 190, 40)
bad = color.rgb(247, 54, 90)

label_font = font.corset
value_font = font.ziplock
title_font = font.ignore

WIDTH = 320
MARGIN = 12
ROW_TOP = 8
ROW_BOTTOM = 192
TITLE_X = 8
TITLE_Y = 202
BAR_HEIGHT = 8
BAR_GAP = 3
VALUE_GAP = 10
SAMPLE_MS = 500
SMOOTH = 0.2
WARN_AT = 75
BAD_AT = 90

load = 0.0
rows = []
sampled_at = -SAMPLE_MS
layout = None


def disk_usage(path):
    try:
        info = os.statvfs(path)
    except OSError:
        return None
    total = info[1] * info[2]
    free = info[3] * info[0]
    if total <= 0:
        return None
    return round(100 * (total - free) / total), f"{(total - free) // 1024} / {total // 1024} KB"


def sample():
    global rows
    gc.collect()
    used = gc.mem_alloc()
    total = used + gc.mem_free()
    rows = [
        ("cpu", round(load), f"{machine.freq() // 1000000} MHz", False),
        ("memory", round(100 * used / total), f"{used // 1024} / {total // 1024} KB", False),
    ]
    flash = disk_usage("/")
    if flash:
        rows.append(("flash", flash[0], flash[1], False))
    state = disk_usage("/state")
    if state and state != flash:
        rows.append(("state", state[0], state[1], False))
    detail = "charging" if badge.is_charging() else "on battery"
    try:
        detail += f"  {badge.battery_voltage():.2f} V"
    except (TypeError, ValueError):
        pass
    rows.append(("battery", round(badge.battery_level()), detail, True))


def measure_layout():
    # font sizes are only known at runtime, so the rows are laid out from measurements
    screen.font = label_font
    _, label_height = screen.measure_text("Ag")
    screen.font = value_font
    for scale in (2, 1):
        value_width, value_height = screen.measure_text("100%", font_size=scale)
        block = label_height + BAR_GAP + BAR_HEIGHT
        pitch = max(block, value_height) + 8
        if pitch * 5 <= ROW_BOTTOM - ROW_TOP:
            break
    return scale, label_height, block, pitch, value_width, value_height


def tone(percent, inverted):
    if inverted:
        percent = 100 - percent
    if percent >= BAD_AT:
        return bad
    if percent >= WARN_AT:
        return warn
    return good


def draw_row(index, label, percent, detail, inverted):
    scale, label_height, block, pitch, value_width, value_height = layout
    top = ROW_TOP + index * pitch
    percent = max(0, min(100, percent))
    left = MARGIN
    right = WIDTH - MARGIN - value_width - VALUE_GAP

    screen.font = label_font
    screen.pen = white
    screen.text(label, left, top)
    detail_width, _ = screen.measure_text(detail)
    screen.pen = dim_white
    screen.text(detail, right - detail_width, top)

    bar_top = top + label_height + BAR_GAP
    screen.pen = track
    screen.rectangle(left, bar_top, right - left, BAR_HEIGHT)
    screen.pen = tone(percent, inverted)
    screen.rectangle(left, bar_top, round((right - left) * percent / 100), BAR_HEIGHT)

    text = f"{percent}%"
    screen.font = value_font
    text_width, _ = screen.measure_text(text, font_size=scale)
    screen.pen = white
    screen.text(text, WIDTH - MARGIN - text_width, top + (block - value_height) / 2, scale)


def update():
    global load, sampled_at, layout
    started = time.ticks_us()

    screen.pen = black
    screen.clear()
    if layout is None:
        layout = measure_layout()

    if badge.ticks - sampled_at >= SAMPLE_MS:
        sampled_at = badge.ticks
        sample()
    for index, row in enumerate(rows):
        draw_row(index, *row)

    screen.font = title_font
    screen.pen = white
    screen.text("machine stats", TITLE_X, TITLE_Y)

    frame_ms = badge.ticks_delta
    busy_ms = time.ticks_diff(time.ticks_us(), started) / 1000
    if frame_ms > 0:
        load += (min(100.0, 100 * busy_ms / frame_ms) - load) * SMOOTH


run(update)
