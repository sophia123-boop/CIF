int pirPin = D3;
int motionState = 0;

void setup() {
  Serial.begin(9600);

  pinMode(pirPin, INPUT);
}

void loop() {
  motionState = digitalRead(pirPin);
  
  if (motionState == HIGH) {
    Serial.println("Motion detected");
  } else {
    Serial.println("No motion");
  }

  delay(250);

}
