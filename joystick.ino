
void readAnalogPin(const char *name, int pin, int mode) {
  pinMode(pin, mode);
  int data = analogRead(pin);
  Serial.print(name);
  Serial.print(":");
  Serial.print(data);
  Serial.print("    ");  
}

void reportButton(const char *name, int pin) {
  readAnalogPin(name, pin, INPUT);
}

void reportAxis(const char *name, int pin) {
  readAnalogPin(name, pin, INPUT_PULLUP);
}

void setup() {
  Serial.begin(9600);
}

const char fire_button[] = "Fire Button:";
const char thumb_button[] = "Thumb Button:";
const char x_axis[] = "X:";
const char y_axis[] = "Y:";

void loop() {
  reportButton(fire_button, A0);
  reportButton(thumb_button, A1);
  reportAxis(x_axis, A2);
  reportAxis(y_axis, A3);
  Serial.println();
  delay(200);
}
