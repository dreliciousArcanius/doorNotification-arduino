const int echo = 6;
const int trigger = 7;


void setup() {
  Serial.begin(9600);
  pinMode(echo, INPUT);
  pinMode(trigger, OUTPUT);
}

void loop() {
  double period, distance;
  digitalWrite(trigger, LOW);
  delayMicroseconds(2);
  digitalWrite(trigger, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger, LOW);
  period = pulseIn(echo, HIGH);
  distance = (period / 2) / 29.1;
  delay(500);

  if (distance < 100) {
      Serial.println(distance);
  } else {
  }
  }
  
