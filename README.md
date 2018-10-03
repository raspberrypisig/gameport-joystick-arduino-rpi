# gameport-joystick-arduino-rpi

## Objective
Connect an old-school retro analog gameport joystick to a raspberry pi so that I can use it as a controller for playing Retropie games.

## Method
1. Grab a MIDI port/gameport from an old sound card and desolder it.
2. Connect MIDI port to joystick, other side to an Arduino
3. Connect Arduino to Pi via USB cable.

## On the Arduino side
Write an Arduino sketch that reads analog values from MIDI port, and send approriate codes over USB (Serial.print statements)
Need to decide on message format to send.

## On the Raspberry Pi side
1. Create a virtual input device using  python evdev library (uinput)
2. Receive data from serial (USB) and send evdev events to Linux input subsystem
3. Configure retropie to recognise the joystick.

## Progress

#### Arduino script
1. At the top of script, I have a DEBUG variable. Set to 1 for displaying raw analog values from buttons/axis (Arduino Uno use 10-bit ADC,
so range of values between 0-1023). Set it to 0 to send actual codes to Raspberry Pi.
2. The message format when DEBUG=0 is two characters, first one identifies button/axis, the second is the value (TODO need to ensure that value is between 0-255 by dividing raw value from analog pins by 4). Also may need to invert result ie. (1023 - raw_value)/4 .    

#### Pi 

1. Can create virtual input device using Python library evdev. It shows up using evtest command, and the capabilities are also shown. 
2. Can get commands from Arduino using pyserial library.
3. Can then pass on values to virtual joystick.
4. Retropie sees it as a gamepad device.

## Annoyances
1. udev rules that I tested on linux mint didn't work on raspbian. I'm not the only one who came across this https://www.raspberrypi.org/forums/viewtopic.php?t=192123 . Solution is to comment out the last 7 lines of /lib/systemd/system/systemd-udevd.service or restart udev after bootup.



