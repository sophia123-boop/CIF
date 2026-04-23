int red_led_pin = D4;

void setup() {
  pinMode(red_led_pin, OUTPUT);
}

void loop() {
  digitalWrite(red_led_pin, HIGH);
}
