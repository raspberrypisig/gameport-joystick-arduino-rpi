from evdev import UInput, ecodes as e
from time import sleep

# https://github.com/torvalds/linux/blob/master/include/uapi/linux/input-event-codes.h

# This script MUST be run as root

class GameportJoystick:
  caps = {
    e.EV_KEY: [
      e.BTN_TRIGGER, e.BTN_THUMB
  ],
    e.EV_ABS: [
      e.ABS_X, e.ABS_Y
  ],
  }

  def __init__(self, name="Gameport Joystick"):
    self.name = name
    self.ui = UInput(events=GameportJoystick.caps, name=name)

  def write(self, type, key, value):
    self.ui.write(type, key, value)
    self.ui.syn()

if __name__ == "__main__":
  joystick = GameportJoystick()
  print("run evtest in another terminal. You have 30 seconds")
  sleep(30)
  print("too late. Pressing trigger button.")
  joystick.write(e.EV_KEY, e.BTN_TRIGGER, 1)
  print("written to virtual input device")
  sleep(30)
