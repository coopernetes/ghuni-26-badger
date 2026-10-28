# Badge firmware modules: `help()` and `dir()` dump

Captured over the USB serial REPL with `mpremote run docs/dump_help.py` on 2026-10-28.
Module headers like `from 'wifi.py'` show the module is frozen Python in firmware, not a file on the USB drive.

## `machine`

```
object <module 'machine'> is of type module
  __name__ -- machine
  mem8 -- <8-bit memory>
  mem16 -- <16-bit memory>
  mem32 -- <32-bit memory>
  mem_backup -- <function>
  unique_id -- <function>
  soft_reset -- <function>
  bootloader -- <function>
  reset -- <function>
  reset_cause -- <function>
  idle -- <function>
  freq -- <function>
  lightsleep -- <function>
  deepsleep -- <function>
  disable_irq -- <function>
  enable_irq -- <function>
  bitstream -- <function>
  dht_readinto -- <function>
  time_pulse_us -- <function>
  Signal -- <class 'Signal'>
  SoftI2C -- <class 'SoftI2C'>
  SoftSPI -- <class 'SoftSPI'>
  ADC -- <class 'ADC'>
  I2C -- <class 'I2C'>
  I2CTarget -- <class 'I2CTarget'>
  I2S -- <class 'I2S'>
  PWM -- <class 'PWM'>
  SPI -- <class 'SPI'>
  UART -- <class 'UART'>
  USBDevice -- <class 'USBDevice'>
  WDT -- <class 'WDT'>
  Pin -- <class 'Pin'>
  RTC -- <class 'RTC'>
  Timer -- <class 'Timer'>
  PWRON_RESET -- 1
  WDT_RESET -- 3
```

**dir():** ADC I2C I2CTarget I2S PWM PWRON_RESET Pin RTC SPI Signal SoftI2C SoftSPI Timer UART USBDevice WDT WDT_RESET bitstream bootloader deepsleep dht_readinto disable_irq enable_irq freq idle lightsleep mem16 mem32 mem8 mem_backup reset reset_cause soft_reset time_pulse_us unique_id

## `micropython`

```
object <module 'micropython'> is of type module
  __name__ -- micropython
  const -- <function>
  opt_level -- <function>
  mem_info -- <function>
  qstr_info -- <function>
  parse_arena -- <function>
  stack_use -- <function>
  alloc_emergency_exception_buf -- <function>
  heap_lock -- <function>
  heap_unlock -- <function>
  kbd_intr -- <function>
  RingIO -- <class 'RingIO'>
  schedule -- <function>
```

**dir():** const RingIO alloc_emergency_exception_buf heap_lock heap_unlock kbd_intr mem_info opt_level parse_arena qstr_info schedule stack_use

## `gc`

```
object <module 'gc'> is of type module
  __name__ -- gc
  collect -- <function>
  disable -- <function>
  enable -- <function>
  isenabled -- <function>
  mem_free -- <function>
  mem_alloc -- <function>
  threshold -- <function>
```

**dir():** collect disable enable isenabled mem_alloc mem_free threshold

## `os`

```
object <module 'os'> is of type module
  __name__ -- os
  sync -- <function>
  uname -- <function>
  urandom -- <function>
  sep -- /
  chdir -- <function>
  getcwd -- <function>
  listdir -- <function>
  mkdir -- <function>
  remove -- <function>
  rename -- <function>
  rmdir -- <function>
  unlink -- <function>
  stat -- <function>
  statvfs -- <function>
  dupterm -- <function>
  dupterm_notify -- <function>
  ilistdir -- <function>
  mount -- <function>
  umount -- <function>
  VfsFat -- <class 'VfsFat'>
  VfsLfs2 -- <class 'VfsLfs2'>
```

**dir():** remove sep VfsFat VfsLfs2 chdir dupterm dupterm_notify getcwd ilistdir listdir mkdir mount rename rmdir stat statvfs sync umount uname unlink urandom

## `time`

```
object <module 'time'> is of type module
  __name__ -- time
  gmtime -- <function>
  localtime -- <function>
  mktime -- <function>
  time -- <function>
  time_ns -- <function>
  sleep -- <function>
  sleep_ms -- <function>
  sleep_us -- <function>
  ticks_ms -- <function>
  ticks_us -- <function>
  ticks_cpu -- <function>
  ticks_add -- <function>
  ticks_diff -- <function>
```

**dir():** gmtime localtime mktime sleep sleep_ms sleep_us ticks_add ticks_cpu ticks_diff ticks_ms ticks_us time time_ns

## `json`

```
object <module 'json'> is of type module
  __name__ -- json
  dump -- <function>
  dumps -- <function>
  load -- <function>
  loads -- <function>
```

**dir():** dump dumps load loads

## `struct`

```
object <module 'struct'> is of type module
  __name__ -- struct
  calcsize -- <function>
  pack -- <function>
  pack_into -- <function>
  unpack -- <function>
  unpack_from -- <function>
```

**dir():** calcsize pack pack_into unpack unpack_from

## `binascii`

```
object <module 'binascii'> is of type module
  __name__ -- binascii
  hexlify -- <function>
  unhexlify -- <function>
  a2b_base64 -- <function>
  b2a_base64 -- <function>
  crc32 -- <function>
```

**dir():** a2b_base64 b2a_base64 crc32 hexlify unhexlify

## `random`

```
object <module 'random'> is of type module
  __name__ -- random
  __init__ -- <function>
  getrandbits -- <function>
  seed -- <function>
  randrange -- <function>
  randint -- <function>
  choice -- <function>
  random -- <function>
  uniform -- <function>
```

**dir():** choice getrandbits randint random randrange seed uniform

## `math`

```
object <module 'math'> is of type module
  __name__ -- math
  e -- 2.718282
  pi -- 3.141592
  tau -- 6.283184
  inf -- inf
  nan -- nan
  sqrt -- <function>
  pow -- <function>
  exp -- <function>
  expm1 -- <function>
  log -- <function>
  log2 -- <function>
  log10 -- <function>
  cosh -- <function>
  sinh -- <function>
  tanh -- <function>
  acosh -- <function>
  asinh -- <function>
  atanh -- <function>
  cos -- <function>
  sin -- <function>
  tan -- <function>
  acos -- <function>
  asin -- <function>
  atan -- <function>
  atan2 -- <function>
  ceil -- <function>
  copysign -- <function>
  fabs -- <function>
  floor -- <function>
  fmod -- <function>
  frexp -- <function>
  ldexp -- <function>
  modf -- <function>
  isfinite -- <function>
  isinf -- <function>
  isnan -- <function>
  isclose -- <function>
  trunc -- <function>
  radians -- <function>
  degrees -- <function>
  factorial -- <function>
  erf -- <function>
  erfc -- <function>
  gamma -- <function>
  lgamma -- <function>
```

**dir():** pow acos acosh asin asinh atan atan2 atanh ceil copysign cos cosh degrees e erf erfc exp expm1 fabs factorial floor fmod frexp gamma inf isclose isfinite isinf isnan ldexp lgamma log log10 log2 modf nan pi radians sin sinh sqrt tan tanh tau trunc

## `array`

```
object <module 'array'> is of type module
  __name__ -- array
  array -- <class 'array'>
```

**dir():** array

## `requests`

```
object <module 'requests' from 'requests/__init__.py'> is of type module
  get -- <function get at 0x1102b420>
  __version__ -- 0.10.2
  __file__ -- requests/__init__.py
  delete -- <function delete at 0x1102b520>
  patch -- <function patch at 0x1102b500>
  __name__ -- requests
  post -- <function post at 0x1102b440>
  socket -- <module 'lwip'>
  Response -- <class 'Response'>
  __path__ -- .frozen/requests
  put -- <function put at 0x1102b4e0>
  request -- <function request at 0x1102b4a0>
  head -- <function head at 0x11025b20>
```

**dir():** get delete put socket Response head patch post request

## `badgeware`

```
object <module 'badgeware' from 'badgeware/__init__.py'> is of type module
  exit_app -- <function exit_app at 0x11022300>
  _run -- <class '_run'>
  get_exception -- <function get_exception at 0x11022560>
  __file__ -- badgeware/__init__.py
  st7789 -- <module 'st7789'>
  sys -- <module 'sys'>
  __name__ -- badgeware
  StringIO -- <class 'StringIO'>
  message -- <function message at 0x110225a0>
  fatal_error -- <function fatal_error at 0x110225c0>
  os -- <module 'os'>
  display -- <ST7789>
  services -- []
  remove_service -- <function remove_service at 0x110222c0>
  running_apps -- []
  reset -- <function reset at 0x110221e0>
  launch -- <function launch at 0x11022540>
  time -- <module 'time'>
  __path__ -- .frozen/badgeware
  set_backlight -- <function set_backlight at 0x11022120>
  k -- tween
  machine -- <module 'machine'>
  gc -- <module 'gc'>
  BACKLIGHT_MIN -- 10
  builtins -- <module 'builtins'>
  v -- <class 'tween'>
  State -- <class 'State'>
  DEFAULT_FONT -- pixel_font("/rom/fonts/sins.ppf")
  _tick_services -- <function _tick_services at 0x11022200>
  current_app -- <function current_app at 0x110222e0>
  get_backlight -- <function get_backlight at 0x110220e0>
  add_service -- <function add_service at 0x110221c0>
  set_brightness -- <function set_brightness at 0x11022040>
  picovector -- <module 'modpicovector'>
  BACKLIGHT_DEFAULT -- 80
```

**dir():** builtins StringIO gc k machine os picovector reset set_brightness st7789 sys time v BACKLIGHT_DEFAULT BACKLIGHT_MIN DEFAULT_FONT State _run _tick_services add_service current_app display exit_app fatal_error get_backlight get_exception launch message remove_service running_apps services set_backlight

## `badgeware.ir`

```
object <module 'badgeware.ir' from 'badgeware/ir.py'> is of type module
  rp2 -- <module 'rp2' from 'rp2.py'>
  SM -- 0
  IR -- <class 'IR'>
  __file__ -- badgeware/ir.py
  IR_RX_PIN -- 17
  badgeware -- <module 'badgeware' from 'badgeware/__init__.py'>
  __name__ -- badgeware.ir
  ir -- <IR object at 1102bf00>
  PIO -- 0
```

**dir():** PIO rp2 IR IR_RX_PIN SM badgeware ir

## `badgeware.link`

```
object <module 'badgeware.link' from 'badgeware/link.py'> is of type module
  PENDING_LIMIT -- 512
  APP -- app
  SERVICE_UUID -- UUID('6e1d0001-8d5c-4b52-9a57-2a6b4c1b0001')
  __file__ -- badgeware/link.py
  SYNC_MS -- 1000
  CASE_LIGHTS -- 4
  FAR_RSSI -- -68
  COMPANY -- b'\xff\xff'
  State -- <class 'State'>
  draw_identicon -- <function draw_identicon at 0x1102c980>
  Link -- <class 'Link'>
  BREATH_HIGH -- 0.45
  INBOX_LIMIT -- 256
  CONNECT_TIMEOUT_MS -- 4000
  SYNC_LEVEL -- 0.5
  const -- <function>
  MAX_CONN_INTERVAL_US -- 15000
  RECEIVE_BUFFER -- 512
  struct -- <module 'struct'>
  bluetooth -- <module 'bluetooth'>
  NAME_LIMIT -- 32
  BADGE_USER_FILE -- /state/badge_user.json
  ADJECTIVES -- ('brave', 'calm', 'eager', 'fuzzy', 'giddy', 'happy', 'jolly', 'keen', 'lucky', 'merry', 'nimble', 'odd', 'plucky', 'quick', 'rusty', 'sly', 'tidy', 'witty', 'zany', 'bold', 'cosmic', 'dizzy', 'feral', 'gentle', 'hasty', 'icy', 'jumpy', 'loud', 'mellow', 'noble', 'perky', 'sunny')
  ADV_INTERVAL_US -- 100000
  ANIMALS -- ('otter', 'badger', 'fox', 'owl', 'newt', 'yak', 'lynx', 'crow', 'mole', 'hare', 'toad', 'wren', 'moth', 'seal', 'goat', 'ibis', 'koala', 'llama', 'mink', 'orca', 'panda', 'quail', 'raven', 'shrew', 'tapir', 'vole', 'bee', 'zebra', 'bison', 'crab', 'dingo', 'eel')
  COOLDOWN_MS -- 8000
  fnv32 -- <function fnv32 at 0x1102cb20>
  badge_name -- <function badge_name at 0x1102c900>
  MESSAGE_UUID -- UUID('6e1d0002-8d5c-4b52-9a57-2a6b4c1b0001')
  DEFAULT_MTU -- 23
  NAME_WAIT_MS -- 500
  SCAN_WINDOW_US -- 20000
  game_code -- <function game_code at 0x1102cb40>
  configured_name -- <function configured_name at 0x1102c920>
  identicon -- <function identicon at 0x1102c940>
  radio -- <Radio object at 1102c3a0>
  badge_id_hex -- <function badge_id_hex at 0x1102c9a0>
  machine -- <module 'machine'>
  BREATH_LOW -- 0.25
  PEER_TIMEOUT_MS -- 3000
  SCAN_INTERVAL_US -- 40000
  split_frames -- <function split_frames at 0x1102c9c0>
  Peer -- <class 'Peer'>
  Proximity -- <class 'Proximity'>
  Lobby -- <class 'Lobby'>
  MAGIC -- b'BL'
  MIN_CONN_INTERVAL_US -- 7500
  VERSION -- 1
  BREATH_MS -- 1600
  __name__ -- badgeware.link
  PREFERRED_MTU -- 247
  RSSI_SMOOTH -- 0.3
  math -- <module 'math'>
  WANT_LEN -- 4
  NO_WANT -- b'\x00\x00\x00\x00'
  NAME_PREFIX -- b'\x00\xffN'
  NEAR_RSSI -- -63
  ID_LEN -- 8
```

**dir():** const bluetooth machine math struct ADJECTIVES ADV_INTERVAL_US ANIMALS APP BADGE_USER_FILE BREATH_HIGH BREATH_LOW BREATH_MS CASE_LIGHTS COMPANY CONNECT_TIMEOUT_MS COOLDOWN_MS DEFAULT_MTU FAR_RSSI ID_LEN INBOX_LIMIT Link Lobby MAGIC MAX_CONN_INTERVAL_US MESSAGE_UUID MIN_CONN_INTERVAL_US NAME_LIMIT NAME_PREFIX NAME_WAIT_MS NEAR_RSSI NO_WANT PEER_TIMEOUT_MS PENDING_LIMIT PREFERRED_MTU Peer Proximity RECEIVE_BUFFER RSSI_SMOOTH SCAN_INTERVAL_US SCAN_WINDOW_US SERVICE_UUID SYNC_LEVEL SYNC_MS State VERSION WANT_LEN badge_id_hex badge_name configured_name draw_identicon fnv32 game_code identicon radio split_frames

## `wifi`

```
object <module 'wifi' from 'wifi.py'> is of type module
  __name__ -- wifi
  nameserver -- <function nameserver at 0x1102e4a0>
  is_connected -- <function is_connected at 0x1102e4e0>
  __file__ -- wifi.py
  RETRY_AFTER_MS -- 20000
  _tick -- <function _tick at 0x1102e380>
  _failure -- None
  network -- <module 'network'>
  ipv4 -- <function ipv4 at 0x1102e500>
  _retries -- 0
  secrets -- <module 'secrets' from 'secrets.py'>
  ipv6 -- <function ipv6 at 0x1102e420>
  ip -- <function ip at 0x1102e440>
  _fail -- <function _fail at 0x1102e2c0>
  gateway -- <function gateway at 0x1102e480>
  _ssid -- None
  connect -- <function connect at 0x1102e3c0>
  get_status -- <function get_status at 0x1102e2a0>
  _timeout_ticks -- None
  subnet -- <function subnet at 0x1102e460>
  failure -- <function failure at 0x1102e2e0>
  NOT_CONFIGURED -- -4
  disconnect -- <function disconnect at 0x1102e3e0>
  wlan -- None
  _retry_at -- 0
  _status_text -- {0: 'Idle', 1: 'Connecting to {ssid}', 2: 'Connected', 3: 'Got IP', -4: 'WiFi is not set up.', -3: 'Incorrect password.', -2: 'Access point {ssid} not found.', -1: 'Connection failed.'}
  status -- <function status at 0x1102e400>
  _psk -- None
  _timeout -- 0
```

**dir():** connect disconnect get_status network status NOT_CONFIGURED RETRY_AFTER_MS _fail _failure _psk _retries _retry_at _ssid _status_text _tick _timeout _timeout_ticks failure gateway ip ipv4 ipv6 is_connected nameserver secrets subnet wlan

## `fetch`

```
object <module 'fetch' from 'fetch.py'> is of type module
  wifi -- <module 'wifi' from 'wifi.py'>
  time -- <module 'time'>
  __file__ -- fetch.py
  _parse_url -- <function _parse_url at 0x1102eb80>
  __name__ -- fetch
  errno -- <module 'errno'>
  io -- <module 'io'>
  url -- <class 'url'>
  tls -- <module 'tls'>
  socket -- <module 'lwip'>
  AsyncFetch -- <class 'AsyncFetch'>
  HTTPException -- <class 'HTTPException'>
  json -- <module 'json'>
```

**dir():** errno io json socket time tls AsyncFetch HTTPException _parse_url url wifi

## `missing_details`

```
object <module 'missing_details' from 'missing_details.py'> is of type module
  __name__ -- missing_details
  missing -- <function missing at 0x110305a0>
  MONA_SANS -- /system/assets/fonts/MonaSans-Medium.af
  __file__ -- missing_details.py
  show -- <function show at 0x11030680>
  shade -- color.rgb(0, 0, 0, 170)
  time -- <module 'time'>
  handle_buttons -- <function handle_buttons at 0x110305e0>
  white -- color.rgb(242, 245, 243, 255)
  black -- color.rgb(0, 0, 0, 255)
  mona_sans -- <function mona_sans at 0x11030560>
  accent -- color.rgb(95, 237, 131, 255)
  HINT_SHAPE -- (Pin(GPIO7, mode=IN, pull=PULL_UP), Pin(GPIO10, mode=IN, pull=PULL_UP))
  HINT_Y -- 222
  draw_hint -- <function draw_hint at 0x11030640>
  draw -- <function draw at 0x11030620>
  HINT_LABEL_SIZE -- 14
  hints -- <module 'hints' from 'hints.py'>
  _mona_sans -- None
  disk_mode -- <function disk_mode at 0x110305c0>
  HINT_STYLE -- <Style object at 11030520>
  muted -- color.rgb(144, 150, 146, 255)
  powman -- <module 'powman'>
  HINT_RADIUS -- 4
```

**dir():** black draw powman show time white HINT_LABEL_SIZE HINT_RADIUS HINT_SHAPE HINT_STYLE HINT_Y MONA_SANS _mona_sans accent disk_mode draw_hint handle_buttons hints missing mona_sans muted shade

## `powman`

```
object <module 'powman'> is of type module
  __name__ -- powman
  sleep -- <function>
  goto_dormant_until -- <function>
  goto_dormant_for -- <function>
  get_wake_reason -- <function>
  get_wake_buttons -- <function>
  shipping_mode -- <function>
  reset_into_msc -- <function>
  _test_psram_cs -- <function>
  WAKE_BUTTON_LEFT -- 0
  WAKE_BUTTON_RIGHT -- 1
  WAKE_BUTTON_SELECT -- 2
  WAKE_BUTTON_UP -- 3
  WAKE_BUTTON_DOWN -- 4
  WAKE_DOUBLETAP -- 5
  WAKE_USER_SW -- 6
  WAKE_VBUS_DETECT -- 7
  WAKE_ALARM -- 240
  WAKE_RESET -- 241
  WAKE_WATCHDOG -- 242
  WAKE_UNKNOWN -- 255
```

**dir():** WAKE_ALARM WAKE_BUTTON_DOWN WAKE_BUTTON_LEFT WAKE_BUTTON_RIGHT WAKE_BUTTON_SELECT WAKE_BUTTON_UP WAKE_DOUBLETAP WAKE_RESET WAKE_UNKNOWN WAKE_USER_SW WAKE_VBUS_DETECT WAKE_WATCHDOG _test_psram_cs get_wake_buttons get_wake_reason goto_dormant_for goto_dormant_until reset_into_msc shipping_mode sleep

## `sparkle`

```
object <module 'sparkle' from 'sparkle.py'> is of type module
  EventState -- <class 'EventState'>
  COLD_SCAN_MS -- 5000
  machine -- <module 'machine'>
  __file__ -- sparkle.py
  HOT_TIMEOUT_MS -- 600000
  time -- <module 'time'>
  RELAY_ADVERTISE_US -- 100000
  LOCAL_TRIGGER_RGB -- 2621751
  SCAN_INTERVAL_US -- 30000
  COLD_GAP_MS -- 55000
  MENU_PATH -- /system/apps/menu
  STATE_KEY -- sparkle_mesh
  HOT_SCAN_MS -- 5000
  LOCAL_TRIGGER_GAP_MS -- 2000
  SHOW_GAP_MS -- 2500
  might_contain_fragment -- <function might_contain_fragment at 0x11032780>
  HELD_SHOW_MS -- 60000
  LOCAL_TRIGGER_DURATION_MS -- 600000
  LOCAL_TRIGGER_SEQUENCE -- (Pin(GPIO7, mode=IN, pull=PULL_UP), Pin(GPIO7, mode=IN, pull=PULL_UP), Pin(GPIO7, mode=IN, pull=PULL_UP), Pin(GPIO7, mode=IN, pull=PULL_UP), Pin(GPIO6, mode=IN, pull=PULL_UP), Pin(GPIO10, mode=IN, pull=PULL_UP))
  SHOW_EXIT_GAP_MS -- 2000
  load_sequence -- <function load_sequence at 0x11032d20>
  SCAN_WINDOW_US -- 30000
  build_advertisement -- <function build_advertisement at 0x110324a0>
  save_sequence -- <function save_sequence at 0x11032d40>
  radio -- <Radio object at 1102c3a0>
  SEQUENCE_MAX -- 4294967295
  RELAY_FRAGMENT_MS -- 180
  RELAY_SCAN_MS -- 500
  service -- None
  request_local_show -- <function request_local_show at 0x11032c40>
  HOT_GAP_MS -- 10000
  QUEUE_LIMIT -- 24
  Gesture -- <class 'Gesture'>
  badgeware -- <module 'badgeware' from 'badgeware/__init__.py'>
  __name__ -- sparkle
  fragment_envelope -- <function fragment_envelope at 0x11032420>
  start -- <function start at 0x11032c00>
  RELAY_ROUNDS -- 2
  SHOW_SCAN_MS -- 2500
  Sparkle -- <class 'Sparkle'>
  resume -- <function resume at 0x11032c20>
  SHOW_EXIT_PRESS_COUNT -- 3
```

**dir():** start machine time COLD_GAP_MS COLD_SCAN_MS EventState Gesture HELD_SHOW_MS HOT_GAP_MS HOT_SCAN_MS HOT_TIMEOUT_MS LOCAL_TRIGGER_DURATION_MS LOCAL_TRIGGER_GAP_MS LOCAL_TRIGGER_RGB LOCAL_TRIGGER_SEQUENCE MENU_PATH QUEUE_LIMIT RELAY_ADVERTISE_US RELAY_FRAGMENT_MS RELAY_ROUNDS RELAY_SCAN_MS SCAN_INTERVAL_US SCAN_WINDOW_US SEQUENCE_MAX SHOW_EXIT_GAP_MS SHOW_EXIT_PRESS_COUNT SHOW_GAP_MS SHOW_SCAN_MS STATE_KEY Sparkle badgeware build_advertisement fragment_envelope load_sequence might_contain_fragment radio request_local_show resume save_sequence service

## `hints`

```
object <module 'hints' from 'hints.py'> is of type module
  pad_parts -- <function pad_parts at 0x110302e0>
  DPAD -- ((Pin(GPIO11, mode=IN, pull=PULL_UP), 0, -1), (Pin(GPIO7, mode=IN, pull=PULL_UP), -1, 0), (Pin(GPIO9, mode=IN, pull=PULL_UP), 1, 0), (Pin(GPIO6, mode=IN, pull=PULL_UP), 0, 1))
  __file__ -- hints.py
  DIRECTIONS -- (Pin(GPIO11, mode=IN, pull=PULL_UP), Pin(GPIO6, mode=IN, pull=PULL_UP), Pin(GPIO7, mode=IN, pull=PULL_UP), Pin(GPIO9, mode=IN, pull=PULL_UP))
  pad_width -- <function pad_width at 0x11030320>
  dpad_offset -- <function dpad_offset at 0x11030300>
  flipped -- <function flipped at 0x11030200>
  spacing_for -- <function spacing_for at 0x11030240>
  PAIR -- (Pin(GPIO10, mode=IN, pull=PULL_UP), BUTTON_BACK)
  DPAD_GAP -- 3
  hint_width -- <function hint_width at 0x11030340>
  Style -- <class 'Style'>
  dot -- <function dot at 0x11030220>
  draw_pair -- <function draw_pair at 0x11030380>
  draw_dpad -- <function draw_dpad at 0x110303a0>
  UPRIGHT_ROW -- (Pin(GPIO7, mode=IN, pull=PULL_UP), Pin(GPIO9, mode=IN, pull=PULL_UP), Pin(GPIO10, mode=IN, pull=PULL_UP))
  hint_height -- <function hint_height at 0x11030360>
  PAIR_SPAN -- 1
  __name__ -- hints
  draw_hint -- <function draw_hint at 0x110303c0>
```

**dir():** dot DIRECTIONS DPAD DPAD_GAP PAIR PAIR_SPAN Style UPRIGHT_ROW dpad_offset draw_dpad draw_hint draw_pair flipped hint_height hint_width pad_parts pad_width spacing_for

## `pairing`

```
object <module 'pairing' from 'pairing.py'> is of type module
  SIGNAL_Y -- 9.4
  SWING_OUT -- (100, 124)
  SCREEN_HEIGHT -- 4.7
  __file__ -- pairing.py
  TOP -- -8.25
  CASE_TOP -- 9.4
  SWING_IN -- (16, 46)
  __name__ -- pairing
  polygon -- <function polygon at 0x11033c60>
  FRONT -- ((color.rgb(119, 58, 114, 255), [<shape>]), (color.rgb(216, 207, 234, 255), [<shape>, <shape>, <shape>]), (color.rgb(119, 58, 114, 255), [<shape>, <shape>, <shape>, <shape>, <shape>, <shape>]))
  CASE_SIDE -- <shape>
  PURPLE -- color.rgb(119, 58, 114, 255)
  PCB_SIDE -- <shape>
  array -- <class 'array'>
  ease -- <function ease at 0x11035100>
  SCREEN_LEFT -- -3.5
  case_outline -- <function case_outline at 0x11033ca0>
  BADGE_HEIGHT -- 16.5
  FRAMES -- 132
  math -- <module 'math'>
  END_ANGLE -- 1.3962632
  button -- <function button at 0x11033cc0>
  CASE_HALF_WIDTH -- 4.25
  SCREEN_WIDTH -- 6.4
  swing -- <function swing at 0x11035120>
  LEAN -- 3.673208
  WEDGE_DEPTH_TOP -- 0.4
  Pairing -- <class 'Pairing'>
  SIGNAL -- (50, 96)
  START_OFFSET -- 5.5
  WEDGE_DEPTH_BOTTOM -- 1.2
  FPS -- 30
  PCB_DEPTH -- 0.16
  PCB_HALF_WIDTH -- 4.0
  LIGHT -- color.rgb(216, 207, 234, 255)
  SCREEN_TOP -- 10.1
```

**dir():** TOP array math BADGE_HEIGHT CASE_HALF_WIDTH CASE_SIDE CASE_TOP END_ANGLE FPS FRAMES FRONT LEAN LIGHT PCB_DEPTH PCB_HALF_WIDTH PCB_SIDE PURPLE Pairing SCREEN_HEIGHT SCREEN_LEFT SCREEN_TOP SCREEN_WIDTH SIGNAL SIGNAL_Y START_OFFSET SWING_IN SWING_OUT WEDGE_DEPTH_BOTTOM WEDGE_DEPTH_TOP button case_outline ease polygon swing

## `easing`

```
object <module 'easing' from 'easing.py'> is of type module
  easeInOutExpo -- <function easeInOutExpo at 0x11035b20>
  easeInSine -- <function easeInSine at 0x11035a80>
  easeInOutQuart -- <function easeInOutQuart at 0x11035a00>
  __file__ -- easing.py
  easeInQuart -- <function easeInQuart at 0x110359c0>
  easeOutQuint -- <function easeOutQuint at 0x11035a40>
  c5 -- 1.3962632
  c1 -- 1.70158
  easeOutSine -- <function easeOutSine at 0x11035aa0>
  easeOutCubic -- <function easeOutCubic at 0x11035980>
  easeOutQuad -- <function easeOutQuad at 0x11035920>
  easeInBounce -- <function easeInBounce at 0x11035c60>
  easeInOutElastic -- <function easeInOutElastic at 0x11035c40>
  easeInOutQuint -- <function easeInOutQuint at 0x11035a60>
  linear -- <function linear at 0x110358c0>
  easeOutElastic -- <function easeOutElastic at 0x11035c20>
  easeOutBounce -- <function easeOutBounce at 0x11035c80>
  easeInExpo -- <function easeInExpo at 0x11035ae0>
  easeInQuad -- <function easeInQuad at 0x11035900>
  easeInOutBounce -- <function easeInOutBounce at 0x11035ca0>
  easeInElastic -- <function easeInElastic at 0x11035c00>
  easeInOutBack -- <function easeInOutBack at 0x11035be0>
  easeInQuint -- <function easeInQuint at 0x11035a20>
  easeOutExpo -- <function easeOutExpo at 0x11035b00>
  cos -- <function>
  pi -- 3.141592
  easeOutQuart -- <function easeOutQuart at 0x110359e0>
  easeInCubic -- <function easeInCubic at 0x11035960>
  easeInBack -- <function easeInBack at 0x11035ba0>
  easeInOutQuad -- <function easeInOutQuad at 0x11035940>
  easeInOutSine -- <function easeInOutSine at 0x11035ac0>
  easeOutBack -- <function easeOutBack at 0x11035bc0>
  easeInOutCubic -- <function easeInOutCubic at 0x110359a0>
  easeOutCirc -- <function easeOutCirc at 0x11035b60>
  __name__ -- easing
  c2 -- 2.594909
  c3 -- 2.70158
  easeInOutCirc -- <function easeInOutCirc at 0x11035b80>
  sin -- <function>
  c4 -- 2.094395
  sqrt -- <function>
  pow -- <function>
  easeInCirc -- <function easeInCirc at 0x11035b40>
```

**dir():** pow cos pi sin sqrt c1 c2 c3 c4 c5 easeInBack easeInBounce easeInCirc easeInCubic easeInElastic easeInExpo easeInOutBack easeInOutBounce easeInOutCirc easeInOutCubic easeInOutElastic easeInOutExpo easeInOutQuad easeInOutQuart easeInOutQuint easeInOutSine easeInQuad easeInQuart easeInQuint easeInSine easeOutBack easeOutBounce easeOutCirc easeOutCubic easeOutElastic easeOutExpo easeOutQuad easeOutQuart easeOutQuint easeOutSine linear

## `pico3d`

```
object <module 'modpico3d'> is of type module
  __name__ -- modpico3d
  vec3 -- <class 'vec3'>
  mat4 -- <class 'mat4'>
  mesh -- <class 'mesh'>
  material -- <class 'material'>
  light -- <class 'light'>
  surface -- <class 'surface'>
  scene -- <class 'scene'>
  engine -- <class 'engine'>
```

**dir():** engine light mat4 material mesh scene surface vec3

## `clock`  (unavailable: ImportError("no module named 'clock'",))

## `tufty`  (unavailable: ImportError("no module named 'tufty'",))

## `global: badge`

```
object <Badge object at 110245a0> is of type Badge
  sleep -- <function sleep at 0x11024500>
  imu_calibrate -- <function imu_calibrate at 0x110241a0>
  __init__ -- <function __init__ at 0x11023ec0>
  pressed -- <function pressed at 0x11024420>
  pressed_to_wake -- <function pressed_to_wake at 0x11024560>
  imu -- <function imu at 0x11024040>
  woken_by_button -- <function woken_by_button at 0x11024540>
  light_level -- <function light_level at 0x110243e0>
  autorotate -- <function autorotate at 0x110240e0>
  _start_internal_i2c -- <function _start_internal_i2c at 0x11023ea0>
  released -- <function released at 0x11024620>
  _merge_touch -- <function _merge_touch at 0x11023fc0>
  wake_reason -- <function wake_reason at 0x11024520>
  poll -- <function poll at 0x11023fa0>
  imu_upright -- <function imu_upright at 0x11024160>
  __qualname__ -- Badge
  woken_by_reset -- <function woken_by_reset at 0x11024580>
  usb_connected -- <function usb_connected at 0x11024340>
  _measure_upside_down -- <function _measure_upside_down at 0x11024000>
  __module__ -- .frozen/badgeware/badge
  is_charging -- <function is_charging at 0x11024380>
  touch_map -- <function touch_map at 0x11024320>
  battery_voltage -- <function battery_voltage at 0x11024460>
  battery_level -- <function battery_level at 0x11024360>
  ticks -- <property>
  upside_down -- <function upside_down at 0x110241c0>
  _refresh_touch_map -- <function _refresh_touch_map at 0x110241e0>
  _load_calibration -- <function _load_calibration at 0x11024020>
  _touch_actions -- <function _touch_actions at 0x11023f60>
  clear -- <function clear at 0x11024240>
  disk_free -- <function disk_free at 0x110243c0>
  direction -- <function direction at 0x110242a0>
  touch -- <function touch at 0x11024140>
  _read_touch -- <function _read_touch at 0x11023f40>
  held -- <function held at 0x110245e0>
  touched -- <function touched at 0x110242e0>
  mode -- <function mode at 0x11024440>
  imu_event -- <function imu_event at 0x11024080>
  ticks_delta -- <property>
  update -- <function update at 0x11024260>
  rotate_180 -- <function rotate_180 at 0x11024120>
  changed -- <function changed at 0x110244a0>
  caselights -- <function caselights at 0x110244c0>
  resolution -- <property>
  _poll_imu -- <function _poll_imu at 0x11023fe0>
```

**dir():** all clear update changed direction held mode model poll pressed released resolution sleep ticks ticks_delta _active_touch_map _autorotate _calibration_loaded _case_light_values _case_lights _current_mode _imu _imu_events _imu_readings _imu_upright _internal_i2c _load_calibration _measure_upside_down _merge_touch _orientation_since _poll_imu _read_touch _refresh_touch_map _rotated _start_internal_i2c _touch _touch_actions _touch_channels _touch_map _upside_down autorotate battery_level battery_voltage buttons caselights default_clear default_pen disk_free first_update imu imu_calibrate imu_event imu_upright is_charging light_level pad pressed_to_wake rotate_180 touch touch_map touched uid upside_down usb_connected wake_reason woken_by_button woken_by_reset

## `global: screen`

```
object image(160 x 120) is of type image
  X4 -- 2
  X2 -- 1
  OFF -- 0
  EVEN_ODD -- 0
  NON_ZERO -- 1
  NEAREST -- 0
  BILINEAR -- 1
  BICUBIC -- 2
  QR_LOW -- 0
  QR_MEDIUM -- 1
  QR_QUARTILE -- 2
  QR_HIGH -- 3
  LEFT -- 0
  CENTER -- 1
  RIGHT -- 2
  TOP -- 0
  MIDDLE -- 1
  BOTTOM -- 2
  CLIP -- 0
  ELLIPSES -- 1
  RGB565 -- 2
  load -- <staticmethod>
  qr -- <staticmethod>
  load_into -- <function>
  window -- <function>
  spritesheet -- <function>
  clear -- <function>
  rectangle -- <function>
  hspan -- <function>
  vspan -- <function>
  line -- <function>
  circle -- <function>
  triangle -- <function>
  blur -- <function>
  bloom -- <function>
  edgeglow -- <function>
  wave -- <function>
  zoom -- <function>
  dither -- <function>
  onebit -- <function>
  monochrome -- <function>
  invert -- <function>
  threshold -- <function>
  saturation -- <function>
  contrast -- <function>
  duotone -- <function>
  crt -- <function>
  grid -- <function>
  vignette -- <function>
  gameboy -- <function>
  noise -- <function>
  glitch -- <function>
  oilpaint -- <function>
  cga -- <function>
  palette_dither -- <function>
  phosphor -- <function>
  synthwave -- <function>
  c64 -- <function>
  nightvision -- <function>
  chromatic -- <function>
  get -- <function>
  put -- <function>
  shape -- <function>
  shapes -- <function>
  text -- <function>
  _set_glyph_registry -- <staticmethod>
  add_glyph -- <staticmethod>
  measure_text -- <function>
  blit -- <function>
  blit_vspan -- <function>
  blit_hspan -- <function>
  batch -- <function>
```

**dir():** clear get BICUBIC BILINEAR BOTTOM CENTER CLIP ELLIPSES EVEN_ODD LEFT MIDDLE NEAREST NON_ZERO OFF QR_HIGH QR_LOW QR_MEDIUM QR_QUARTILE RGB565 RIGHT TOP X2 X4 _set_glyph_registry add_glyph alpha antialias batch blit blit_hspan blit_vspan bloom blur c64 cga chromatic circle clip contrast crt cursor dither duotone edgeglow fill_rule font gameboy glitch grid has_palette height hspan invert line load load_into measure_text monochrome nightvision noise oilpaint onebit palette palette_dither palette_size pen phosphor put qr raw rectangle saturation shape shapes spritesheet stride synthwave text threshold triangle vignette vspan wave width window zoom

## `global: image`

```
object <class 'image'> is of type type
  X4 -- 2
  X2 -- 1
  OFF -- 0
  EVEN_ODD -- 0
  NON_ZERO -- 1
  NEAREST -- 0
  BILINEAR -- 1
  BICUBIC -- 2
  QR_LOW -- 0
  QR_MEDIUM -- 1
  QR_QUARTILE -- 2
  QR_HIGH -- 3
  LEFT -- 0
  CENTER -- 1
  RIGHT -- 2
  TOP -- 0
  MIDDLE -- 1
  BOTTOM -- 2
  CLIP -- 0
  ELLIPSES -- 1
  RGB565 -- 2
  load -- <staticmethod>
  qr -- <staticmethod>
  load_into -- <function>
  window -- <function>
  spritesheet -- <function>
  clear -- <function>
  rectangle -- <function>
  hspan -- <function>
  vspan -- <function>
  line -- <function>
  circle -- <function>
  triangle -- <function>
  blur -- <function>
  bloom -- <function>
  edgeglow -- <function>
  wave -- <function>
  zoom -- <function>
  dither -- <function>
  onebit -- <function>
  monochrome -- <function>
  invert -- <function>
  threshold -- <function>
  saturation -- <function>
  contrast -- <function>
  duotone -- <function>
  crt -- <function>
  grid -- <function>
  vignette -- <function>
  gameboy -- <function>
  noise -- <function>
  glitch -- <function>
  oilpaint -- <function>
  cga -- <function>
  palette_dither -- <function>
  phosphor -- <function>
  synthwave -- <function>
  c64 -- <function>
  nightvision -- <function>
  chromatic -- <function>
  get -- <function>
  put -- <function>
  shape -- <function>
  shapes -- <function>
  text -- <function>
  _set_glyph_registry -- <staticmethod>
  add_glyph -- <staticmethod>
  measure_text -- <function>
  blit -- <function>
  blit_vspan -- <function>
  blit_hspan -- <function>
  batch -- <function>
```

**dir():** clear get BICUBIC BILINEAR BOTTOM CENTER CLIP ELLIPSES EVEN_ODD LEFT MIDDLE NEAREST NON_ZERO OFF QR_HIGH QR_LOW QR_MEDIUM QR_QUARTILE RGB565 RIGHT TOP X2 X4 _set_glyph_registry add_glyph batch blit blit_hspan blit_vspan bloom blur c64 cga chromatic circle contrast crt dither duotone edgeglow gameboy glitch grid hspan invert line load load_into measure_text monochrome nightvision noise oilpaint onebit palette_dither phosphor put qr rectangle saturation shape shapes spritesheet synthwave text threshold triangle vignette vspan wave window zoom

## `global: shape`

```
object <class 'shape'> is of type type
  ALIGN_OUTER -- 0
  ALIGN_INNER -- 1
  ALIGN_CENTER -- 2
  PATH_CLOSED -- 0
  PATH_OPEN -- 4
  JOIN_MITER -- 0
  JOIN_ROUND -- 8
  JOIN_BEVEL -- 16
  CAP_BUTT -- 0
  CAP_ROUND -- 32
  CAP_SQUARE -- 64
  custom -- <staticmethod>
  combine -- <staticmethod>
  regular_polygon -- <staticmethod>
  circle -- <staticmethod>
  ellipse -- <staticmethod>
  rectangle -- <staticmethod>
  rounded_rectangle -- <staticmethod>
  squircle -- <staticmethod>
  arc -- <staticmethod>
  pie -- <staticmethod>
  star -- <staticmethod>
  line -- <staticmethod>
  stroke -- <function>
  grow -- <function>
  shrink -- <function>
  bounds -- <function>
```

**dir():** ALIGN_CENTER ALIGN_INNER ALIGN_OUTER CAP_BUTT CAP_ROUND CAP_SQUARE JOIN_BEVEL JOIN_MITER JOIN_ROUND PATH_CLOSED PATH_OPEN arc bounds circle combine custom ellipse grow line pie rectangle regular_polygon rounded_rectangle shrink squircle star stroke

## `global: color`

```
object <class 'color'> is of type type
  COMPLEMENT -- 0
  SPLIT -- 1
  TRIAD -- 2
  TETRAD -- 3
  SQUARE -- 4
  ANALOGOUS -- 5
  black -- color.rgb(20, 30, 40, 255)
  grape -- color.rgb(68, 36, 52, 255)
  navy -- color.rgb(48, 52, 109, 255)
  grey -- color.rgb(78, 74, 78, 255)
  brown -- color.rgb(133, 76, 48, 255)
  green -- color.rgb(52, 101, 36, 255)
  red -- color.rgb(208, 70, 72, 255)
  taupe -- color.rgb(117, 113, 97, 255)
  blue -- color.rgb(89, 125, 206, 255)
  orange -- color.rgb(210, 125, 44, 255)
  smoke -- color.rgb(133, 149, 161, 255)
  lime -- color.rgb(109, 170, 44, 255)
  latte -- color.rgb(210, 170, 153, 255)
  cyan -- color.rgb(109, 194, 202, 255)
  yellow -- color.rgb(218, 212, 94, 255)
  white -- color.rgb(222, 238, 214, 255)
  transparent -- color.rgb(0, 0, 0, 0)
  light_grey -- color.rgb(192, 192, 192, 255)
  dark_grey -- color.rgb(64, 64, 64, 255)
  rgb -- <staticmethod>
  hsv -- <staticmethod>
  oklch -- <staticmethod>
  to_oklch -- <function>
  to_rgb -- <function>
  contrast -- <function>
  difference -- <function>
  fit -- <function>
  ramp -- <staticmethod>
  max_chroma -- <staticmethod>
  rotate -- <function>
  saturate -- <function>
  harmony -- <function>
  tones -- <function>
  readable_on -- <function>
  lighten -- <function>
  darken -- <function>
  scale -- <function>
  with_alpha -- <function>
  mix -- <function>
  over -- <function>
```

**dir():** ANALOGOUS COMPLEMENT SPLIT SQUARE TETRAD TRIAD black blue brown contrast cyan dark_grey darken difference fit grape green grey harmony hsv latte light_grey lighten lime max_chroma mix navy oklch orange over ramp readable_on red rgb rotate saturate scale smoke taupe to_oklch to_rgb tones transparent white with_alpha yellow

## `global: brush`

```
object <class 'brush'> is of type type
  LINEAR -- 0
  RADIAL -- 1
  CONICAL -- 2
  pattern -- <staticmethod>
  image -- <staticmethod>
  gradient -- <staticmethod>
  geometry -- <function>
  fractal -- <staticmethod>
  ramp -- <function>
  erase -- <staticmethod>
  pixelate -- <staticmethod>
  blur -- <staticmethod>
  lighten -- <staticmethod>
  darken -- <staticmethod>
  monochrome -- <staticmethod>
  dither -- <staticmethod>
  palette_dither -- <staticmethod>
  invert -- <staticmethod>
  threshold -- <staticmethod>
  saturation -- <staticmethod>
  contrast -- <staticmethod>
  duotone -- <staticmethod>
  crt -- <staticmethod>
  grid -- <staticmethod>
  vignette -- <staticmethod>
  noise -- <staticmethod>
  glitch -- <staticmethod>
  oilpaint -- <staticmethod>
  phosphor -- <staticmethod>
  nightvision -- <staticmethod>
  chromatic -- <staticmethod>
```

**dir():** CONICAL LINEAR RADIAL blur chromatic contrast crt darken dither duotone erase fractal geometry glitch gradient grid image invert lighten monochrome nightvision noise oilpaint palette_dither pattern phosphor pixelate ramp saturation threshold vignette

## `global: mat3`

```
object <class 'mat3'> is of type type
  trs -- <staticmethod>
  rotate -- <function>
  rotate_radians -- <function>
  translate -- <function>
  scale -- <function>
  multiply -- <function>
  inverse -- <function>
```

**dir():** inverse multiply rotate rotate_radians scale translate trs

## `global: font`

```
object <font> is of type font
```

**dir():** absolute ark awesome bacteria badgeware badgewaremax compass corset cosmetics cosmetics_outline curse desert emoji emoji_outline fear food food_outline futile hats hats_outline holotype hungry ignore kobold lookout loser manticore match memo more nope outflank saga salty sins smart teatime tools_crafting tools_crafting_outline torch travel travel_outline troll unfair vest weather weather_outline winds yesterday yolk ziplock

## `global: display`

```
object <ST7789> is of type ST7789
  __del__ -- <function>
  update -- <function>
  fullres -- <function>
  backlight -- <function>
  command -- <function>
  set_max_pio_clock -- <function>
  set_vsync -- <function>
  set_async -- <function>
  deferred_clear -- <function>
  set_rotate_180 -- <function>
  set_framerate -- <function>
```

**dir():** update HEIGHT WIDTH backlight command deferred_clear fullres set_async set_framerate set_max_pio_clock set_rotate_180 set_vsync

## `global: rect`

```
object <class 'rect'> is of type type
  deflate -- <function>
  inflate -- <function>
  intersection -- <function>
  intersects -- <function>
  empty -- <function>
  offset -- <function>
  contains -- <function>
```

**dir():** contains deflate empty inflate intersection intersects offset

## `global: run`

```
object <class '_run'> is of type type
  progress -- <property>
  ticks -- <property>
  __init__ -- <function __init__ at 0x110224a0>
  __module__ -- badgeware
  __call__ -- <function __call__ at 0x11022420>
  __qualname__ -- _run
```

**dir():** ticks progress

## `global: launch`

```
object <function launch at 0x11022540> is of type function
```

## `global: State`

```
object <class 'State'> is of type type
  delete -- <staticmethod>
  modify -- <staticmethod>
  save -- <staticmethod>
  __module__ -- .frozen/badgeware/state
  load -- <staticmethod>
  __qualname__ -- State
```

**dir():** delete load modify save

