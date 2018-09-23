# gameport-joystick-arduino-rpi

## Objective
Connect to old retro gameport joystick to a raspberry pi so I can use it as a controller for playing Retropie games.

## Method

1. Grab a MIDI port/gameport from an old sound card and desolder it.
2. Connect MIDI port to joystick, other side to an Arduino
3. Connect Arduino to Pi via USB cable.

## On the Arduino side
Write an Arduino sketch that reads analog values from MIDI port, and send approriate codes over USB (Serial.print statements)
Need to decide on message format to send.

## On the Raspberry Pi side
1. Create a virtual serial port using  python evdev library (uinput)
2. Receive data from serial (USB) and send evdev events to Linux input subsystem
3. Configure retropie to recognise the joystick.




