# Badge controls

Two input sources feed the same button names (`BUTTON_UP`, `BUTTON_SELECT`, ...):

- **`badge.buttons`**: the six physical buttons on the SoC (the detachable part).
- **`badge.pad`**: the touch controller board (d-pad, two round buttons, two middle pills).

`badge.pressed(...)` and `badge.held(...)` see both. Apps can also read one source alone.

Status key: **verified** = confirmed on the badge, **inferred** = read from firmware/app code, not tried.

## Physical buttons (SoC)

Pin names come from the firmware dump in [`modules.md`](modules.md) (`BUTTON_*` objects, `hints`). The glyph positions are from a photo of the board.

| Button | Where | Pin | Status |
|---|---|---|---|
| `BUTTON_UP` | right edge, top | GPIO11 | verified (pin), inferred (position) |
| `BUTTON_DOWN` | right edge, bottom | GPIO6 | verified (pin), inferred (position) |
| `BUTTON_LEFT` | bottom row, left (`<`) | GPIO7 | verified (pin) |
| `BUTTON_RIGHT` | bottom row, middle (`>`) | GPIO9 | verified (pin) |
| `BUTTON_SELECT` ("Enter") | bottom row, right (`↩`) | GPIO10 | verified (pin) |
| `BUTTON_HOME` | back of the SoC | GPIO22 | inferred |

There is no physical `BUTTON_BACK` or `BUTTON_MENU`. Those exist only on the touch controller.

## Touch controller

`badge.touch_map()` maps touch channels to buttons (verified):

| Channel | Button | On the board |
|---|---|---|
| 0 | `BUTTON_UP` | d-pad up |
| 1 | `BUTTON_RIGHT` | d-pad right |
| 2 | `BUTTON_DOWN` | d-pad down |
| 3 | `BUTTON_LEFT` | d-pad left |
| 4 | `BUTTON_MENU` | **right middle pill (white)**, verified by live press |
| 5 | `BUTTON_HOME` | **left middle pill (gold)**, inferred (it is the other pill, and it shares the HOME pin's button) |
| 6 | `BUTTON_SELECT` | one of the two round buttons |
| 7 | `BUTTON_BACK` | the other round button |

Which round button (gold or white) is Select and which is Back is not confirmed.

The touch controller is not reachable when the laminated badge card is attached over the SoC, which is why the SoC buttons also get their own shortcuts.

## Main menu

| Input | Action |
|---|---|
| Up / Down | Move through the list |
| Right | Open the highlighted submenu (or the Expedition award picker) |
| Left | Go back out of a submenu (does nothing at the top level) |
| Select / Enter | Open a submenu, open the award picker, or launch the app |
| Back (touch only) | Same as Left |

In the Expedition award picker, Left and Right move between awards and Select picks one.

## Leaving an app

| Input | Action | Works in a frozen app? |
|---|---|---|
| Hold **Left + Enter** on the SoC for 1 s | Reset back to the menu | Yes. The pins are read by a 50 ms timer, not by the app |
| Hold the **right middle pill (MENU)** for 0.4 s | Reset back to the menu | Only if the app still polls buttons (it reads the pad's cached state) |
| Back of the SoC (`HOME`) / left middle pill | App-specific. Some apps (Rogue, Merge Conflict) handle it themselves; others ignore it | No |

Both shortcuts are installed in `main.py` just before an app launches, so they are not active in the menu itself. A quick tap on the right pill still reaches the app, so Rogue's in-game menu keeps working.

Caveats:

- Pong and Brattal use Left and Enter as game controls, so holding both for a full second there will drop you out.
- The reset path skips an app's own `on_exit`. Rogue's autosave does not run on it.
- Neither shortcut has been tried on the badge yet.

## USB

The badge shows up as one composite device, vendor `2e8a` product `1101`:

- A serial REPL at `/dev/ttyACM0` (for `mpremote`).
- A mass-storage drive, which can be mounted while the badge runs normally.

Linux resets the permissions on `/dev/ttyACM0` to `root:dialout 0660` on every replug. A udev rule fixes it permanently:

```
SUBSYSTEM=="tty", ATTRS{idVendor}=="2e8a", ATTRS{idProduct}=="1101", MODE="0666"
```

Writing files from the PC while the badge's own firmware has the flash mounted can corrupt the filesystem. Put the badge into disk mode with the Mass Storage app first, then eject cleanly.
