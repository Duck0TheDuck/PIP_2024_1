//initializing LED 
int led_pin = 6;

void setup() {
  //Declaring LED pin as output
  pinMode(led_pin, OUTPUT);
}

void loop() {
  // Enciende el LED
  digitalWrite(led_pin, HIGH); // Enciende el LED
  delay(3000); // Espera 3 segundos

  // Apaga el LED
  digitalWrite(led_pin, LOW); // Apaga el LED
  delay(3000); // Espera 3 segundos
}
