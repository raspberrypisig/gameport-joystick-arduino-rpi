from evdev import UInput, AbsInfo, ecodes as e
from time import sleep
import serial

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
    
    
  def read(self):
    data = self.serial.read(2)
    data = str(data)
    command = data[0]
    value = data[1]

    if command == 'x':
      print(value)

    elif command == 'y':
      pass

    elif command == 'f':
      pass

    elif command == 't':
      pass


if __name__ == "__main__":
  arduino = ArduinoSerial('/dev/tty30')
  while True:
    arduino.read()



