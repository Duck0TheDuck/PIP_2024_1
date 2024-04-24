byte buffer [13];
void setup()
{
  Serial.begin(9600);
}
void loop()
{
  if(Serial.available()){
    Serial.readBytesUntil('\n',buffer, 13);
    Serial.write(buffer,13);
  }
}