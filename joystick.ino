
void readAnalogPin(char *name, int pin) {
  pinMode(pin, INPUT_PULLUP);
  int data = analogRead(pin);
  Serial.print(name);
  Serial.print(":");
  Serial.print(data);
  Serial.print("    ");  
}

void readButton1() {
  readAnalogPin("button1", A0);
}

void readButton2() {
  readAnalogPin("button2", A1);
}

void readXAxis() {
  readAnalogPin("x-axis", A2);
}

void readYAxis() {
  readAnalogPin("y-axis", A3);
}

void setup() {
  Serial.begin(9600);
}

int data;

void loop() {
  readButton1();
  readButton2();
  readXAxis();
  readYAxis();
  Serial.println();
  delay(200);
}
