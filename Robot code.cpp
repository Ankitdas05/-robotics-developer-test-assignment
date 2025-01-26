void setup() {
    int ledPins[] = {27, 25, 33, 21, 26, 23, 22, 12, 19, 13};
    for (int i = 0; i < 10; i++) {
        pinMode(ledPins[i], OUTPUT);
        digitalWrite(ledPins[i], LOW);
    }
}

void loop() {
    int ledPins[] = {27, 25, 33, 21, 26, 23, 22, 12, 19, 13};
    for (int i = 0; i < 10; i++) {
        digitalWrite(ledPins[i], HIGH);
        delay(300);
        digitalWrite(ledPins[i], LOW);
    }
}
