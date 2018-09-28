#define DEBUG 0
//#define DEBUG 1

#define TRIGGER_BUTTON_PIN A0
#define THUMB_BUTTON_PIN A1
#define X_AXIS_PIN A2
#define Y_AXIS_PIN A3

#define BUTTON_THRESHOLD 900 //This determines if button is pressed or not (900/1024 * 5V)

void print_debug_message(const char *name, int value) {
    Serial.print(name);
    Serial.print(":");
    Serial.print(value);
    Serial.print("    "); 
}

int TriggerButtonPreviousValue = 0;
int ThumbsButtonPreviousValue = 0;
int XAxisPreviousValue = 0;
int YAxisPreviousValue = 0;

int buttonValueToSend(int value) {
  if (value > BUTTON_THRESHOLD) {
    return 0;
  }

  else {
    return 1;
  }
}

int axisValueToSend(int value) {
  if (value < BUTTON_THRESHOLD) {
    return 0;
  }

  else {
    return 1;
  }
}

void sendButton(char command, int pinValue, int *previousValue) {
  int currentButtonValue;  
      
  currentButtonValue = buttonValueToSend(pinValue);
  
  if (currentButtonValue != *previousValue) {
    Serial.print(command);
    Serial.print(currentButtonValue);
  }
      
  *previousValue = currentButtonValue;
}

void sendAxis(char command, int pinValue, int *previousValue) {
  int currentAxisValue;  
      
  currentAxisValue = axisValueToSend(pinValue);
  
  if (currentAxisValue != *previousValue) {
    Serial.print(command);
    Serial.print(currentAxisValue);
  }
      
  *previousValue = currentAxisValue;
}


void send_movement(int pin, int pinValue) { 
 
  
  switch(pin){
    case A0:
      sendButton('a', pinValue, &TriggerButtonPreviousValue);
      break;

    case A1:
      sendButton('b', pinValue, &ThumbsButtonPreviousValue);
      break;

    case A2:
      sendAxis('x', pinValue, &XAxisPreviousValue);
      break;

    case A3:
      sendAxis('y', pinValue, &YAxisPreviousValue);
      break;
  }
}

int readAnalogPin(int pin, int mode) {
  pinMode(pin, mode);
  int pinValue = analogRead(pin);
  return pinValue;
}

void reportButtonOrAxis(const char *name, int pin) {
  int pinValue = readAnalogPin(pin, INPUT_PULLUP);
  if (DEBUG) {
    print_debug_message(name, pinValue);
  }

  else {
    send_movement(pin, pinValue);
  }
}

const char trigger_button[] = "Fire Button:";
const char thumb_button[] = "Thumb Button:";
const char x_axis[] = "X:";
const char y_axis[] = "Y:";

void gatherJoystickData() {
  reportButtonOrAxis(trigger_button, TRIGGER_BUTTON_PIN);
  reportButtonOrAxis(thumb_button, THUMB_BUTTON_PIN);
  reportButtonOrAxis(x_axis, X_AXIS_PIN);
  reportButtonOrAxis(y_axis, Y_AXIS_PIN);
}

void setup() {
  Serial.begin(9600);
}

void loop() {
  gatherJoystickData();
  
  if (DEBUG) {
    Serial.println();
    delay(200);
  }

  else {
    delay(100);
  }
  
}
