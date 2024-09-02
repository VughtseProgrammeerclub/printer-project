int pinStart = 13;
int pinTacho = 12;
int pinDot01 = 11;
bool pinTachoState = false;
bool pinStartState = LOW;
bool lastPinTachoState = LOW;
int tachoPulsen = 0;
unsigned long millisStart;
unsigned long millisNu;
unsigned long microsNu;
unsigned long microsStartDot;
bool dotPulsGestart = false;
bool dotTimerLoopt = false;

void setup() {
  pinMode(pinStart, OUTPUT);
  pinMode(pinTacho, INPUT);
  pinMode(pinDot01, OUTPUT);
  Serial.begin(115200);  // Start de seriële communicatie met 9600 baud
}

void loop() {
  millisNu = millis();
  if (millisNu - millisStart > 500) {
    if (pinStartState == HIGH) {
      tachoPulsen = 0;
      pinStartState = LOW;
      millisStart = millisNu;
    }
    if (millisNu - millisStart > 2500) {
      if (pinStartState == LOW) {
        pinStartState = HIGH;
        millisStart = millisNu;
        Serial.println(tachoPulsen);  // Print de waarde van tachoPulsen naar de seriële monitor
      }
    }
  }
  // Controleer de status van de pinTacho
  pinTachoState = digitalRead(pinTacho);

  // Als de huidige status HIGH is en de vorige status LOW, dan is er een puls gedetecteerd
  //if (pinTachoState == HIGH && lastPinTachoState == LOW) {
  if (pinTachoState != lastPinTachoState) {
    tachoPulsen++;
    dotPulsGestart = true;
    dotTimerLoopt = true;
  }

  // Update de laatste status van pinTacho
  lastPinTachoState = pinTachoState;

  digitalWrite(pinStart, pinStartState);

  microsNu = micros();
  if (dotPulsGestart == true) {
    digitalWrite(pinDot01, HIGH);
  }
  if (dotTimerLoopt == true) {
    microsStartDot = microsNu;
    dotTimerLoopt = false;
  }
  if (microsNu - microsStartDot > 1500) {
    digitalWrite(pinDot01, LOW);
    dotPulsGestart = false;
    dotTimerLoopt = false;
  }
}
