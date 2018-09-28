from evdev import UInput, AbsInfo, ecodes as e
from time import sleep
import serial
from GameportJoystick import GameportJoystick

'''
In read function:

command is 2-byte

second byte is value
first byte is one of x(x-axis) , y(y-axis), f(fire/top button), t(thumb button)

Buttons:
the value will be 0 for off, 1 for on

Axis:
the value will be 0 for center, 1 for negative direction, 2 for positive direction

'''

class ArduinoSerial:
  def __init__(self, port):
    self.serial = serial.Serial(port)
    self.joystick = GameportJoystick()

  def read(self):
    data = self.serial.read(2)
    data = str(data)
    command = data[0]
    value = int(data[1])

    if command == 'x':
      print('x', value)
      self.joystick.write(e.EV_ABS, e.ABS_X, value)

    elif command == 'y':
      print('y', value)
      self.joystick.write(e.EV_ABS, e.ABS_Y, value)


    elif command == 'a':
      print('a', value)
      self.joystick.write(e.EV_KEY, e.BTN_TRIGGER, value)

    elif command == 'b':
      print('b', value)
      self.joystick.write(e.EV_KEY, e.BTN_THUMB, value)


if __name__ == "__main__":
  arduino = ArduinoSerial('/dev/ttyACM0')
  while True:
    arduino.read()
