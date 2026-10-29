# Recovering a badge that fails at startup

If a bad file on the badge stops the menu loading, the USB disk never mounts, so the usual copy-files fix is out. The serial REPL still answers, and from there you can reboot the badge into disk mode.

Status key: **verified** = done on the badge during the incident below, **unverified** = reasoned from the code, not tried.

## Symptoms

The badge shows a startup error instead of the menu, for example `ImportError: no module named ...` or `can't import name ICONS`. Plugging it in shows no usable drive (`lsblk` reports `sda` at 0 B, "media removed"), but `/dev/ttyACM0` is present.

## Recovery

You need the repo's `.venv` with `mpremote` (`python3 -m venv .venv && .venv/bin/pip install mpremote`).

1. **Open the serial port.** Linux resets its permissions on every replug.
   ```
   sudo chmod a+rw /dev/ttyACM0
   ```
   To make it permanent, add a udev rule (verified to match this badge's IDs, vendor `2e8a`, product `1101`):
   ```
   SUBSYSTEM=="tty", ATTRS{idVendor}=="2e8a", ATTRS{idProduct}=="1101", MODE="0666"
   ```
   in `/etc/udev/rules.d/99-badger.rules`, then `sudo udevadm control --reload && sudo udevadm trigger`.

2. **Check you can reach it.** (verified)
   ```
   .venv/bin/mpremote connect /dev/ttyACM0 exec "import os; print(os.listdir('/system/apps/menu'))"
   ```

3. **Reboot into disk mode.** (verified) The filesystem is read-only from the REPL (`OSError: 30`), so editing it from there fails. The Mass Storage app switches to disk mode with one call, and you can make the same call by hand:
   ```
   .venv/bin/mpremote connect /dev/ttyACM0 exec "import powman; powman.reset_into_msc()"
   ```
   The command prints `OSError: [Errno 5] Input/output error`. That is the connection dropping as the badge reboots, not a failure. After a few seconds the drive mounts as `BADGER`.

4. **Fix the files on the drive.** Copy the known-good versions from this repo (or from `original-files/`, the pre-change copy of everything on the badge) over the bad ones. Compare the result:
   ```
   cmp apps/menu/app.py /run/media/$USER/BADGER/apps/menu/app.py
   sync
   ```

5. **Eject and reboot.** `udisksctl unmount -b /dev/sda`, then power-cycle the badge.

If you only need to undo everything, copy `original-files/` back over the drive (leave `secrets.py` alone, since it is not tracked and holds your WiFi details).

### If the serial port is unreachable

The badge's own documentation (the simulator page, saved in [`badger-site/simulator.md`](badger-site/simulator.md)) says to quickly
press RESET twice to get USB Disk Mode, then wait for the BADGER drive. That should mount the drive even when the menu will not
start. I read this on the site but did not try it, because the serial route worked.

## Cause of the incident this was written for

An icon folder named `apps/menu/icons/` sat next to the compiled module `icons.mpy`. MicroPython resolves a directory before a module of the same name, so `from icons import ICONS` failed and the menu would not start. The folder is now `apps/menu/pictures/`.

Do not name a new file or folder after an existing module. The menu imports `ui`, `icons`, `gallery`, `app`, `silhouettes`, `achievements`, `celebration`, `opening`, `mona3d`, `mona` and `banner`, and other apps import `hints`, `pairing`, `missing_details` and more (see `docs/modules.md`).

## Notes

- The device root also holds `.fsbackup` and `.fsbackup.crc32`. I did not touch them and don't know what they do. They may be a firmware-managed backup of `/system`, so look before assuming a bad edit is permanent.
- Writing to the drive from the PC while the badge is running normally can corrupt the filesystem. The kernel already logged `Volume was not properly unmounted` after earlier sessions. Prefer entering disk mode properly, then ejecting cleanly.
- Each `mpremote exec` interrupts the running app, which ends in a reset back to the menu. That is expected.
