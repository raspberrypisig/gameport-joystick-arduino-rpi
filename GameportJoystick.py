from evdev import UInput, AbsInfo, ecodes as e
from time import sleep

# https://github.com/torvalds/linux/blob/master/include/uapi/linux/input-event-codes.h

# This script MUST be run as root


class GameportJoystick:
  caps = {
    e.EV_KEY: [
      e.BTN_TRIGGER, e.BTN_THUMB
  ],
    e.EV_ABS: [
      (e.ABS_X, AbsInfo(value=0, min=0, max=1024, fuzz=0, flat=0, resolution=0)),
      (e.ABS_Y, AbsInfo(value=0, min=0, max=1024, fuzz=0, flat=0, resolution=0))
  ],
  }

  def __init__(self, name="Gameport Joystick"):
    self.name = name
    self.ui = UInput(events=GameportJoystick.caps, name=name)

  def write(self, type, key, value):
    self.ui.write(type, key, value)
    self.ui.syn()

  def pressAndHoldTriggerButton(self):
    toggle=0
    for i in range(1000):
      self.ui.write(e.EV_KEY, e.BTN_TRIGGER, toggle)
      self.ui.syn()
      toggle = 1 - toggle

if __name__ == "__main__":
  joystick = GameportJoystick()
  print("run evtest in another terminal. You have 30 seconds")
  sleep(30)
  print("too late. Pressing trigger button.")
  joystick.write(e.EV_KEY, e.BTN_TRIGGER, 1)
  print("written to virtual input device")
  print("Go to retropie and Hit menu button->Configure Input")
  joystick.pressAndHoldTriggerButton()
  sleep(30)
