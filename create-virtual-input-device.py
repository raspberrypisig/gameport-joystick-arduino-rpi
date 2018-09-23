from evdev import UInput, ecodes as e
from time import sleep

# https://github.com/torvalds/linux/blob/master/include/uapi/linux/input-event-codes.h

caps = {
  e.EV_KEY: [
    e.BTN_TRIGGER, e.BTN_THUMB
  ],
  e.EV_ABS: [
    e.ABS_X, e.ABS_Y
  ],
}

ui = UInput(events=caps, name="Gameport Joystick")
sleep(30)
ui.close()
