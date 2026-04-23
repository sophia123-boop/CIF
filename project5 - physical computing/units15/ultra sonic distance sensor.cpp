int trigPin = D1; 
int echoPin = D2;
long soundTravelTime, distance;


void setup() {
 Serial.begin(9600);
 pinMode(trigPin, OUTPUT);
 pinMode(echoPin, INPUT);
}


void loop() {
 digitalWrite(trigPin, LOW);
 delayMicroseconds(5);
 digitalWrite(trigPin, HIGH);
 delayMicroseconds(10);
 digitalWrite(trigPin, LOW);


 soundTravelTime = pulseIn(echoPin, HIGH);
  distance = (soundTravelTime/2) * 0.034;


 Serial.print("Distance: ");
 Serial.print(distance);
 Serial.println(" cm");
 Serial.println();


 delay(250);
}
