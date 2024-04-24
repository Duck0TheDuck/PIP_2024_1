int led[] = {2, 3, 4, 5, 6, 7, 8, 9};
bool estado[] = {false, false, false, false, false, false, false, false};

void setup() {
  for(int i = 0; i < 8; i++) {
    pinMode(led[i], OUTPUT);
  }
}

void loop() {
  
  for(int count = 1; count <= 255; count++) {
    
    for(int i = 0; i < 8; i++) {
      estado[7 - i] = bitRead(count, i);
    }

    
    for(int i = 0; i < 8; i++) {
      digitalWrite(led[i], estado[i]);
    }

    
    delay(1000);
  }
}
