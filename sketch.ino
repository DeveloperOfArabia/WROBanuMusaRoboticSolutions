int soilMoisturePin = A0;
int ldrPin = A1;
int ntcPin = A2;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int soilMoistureValue = analogRead(soilMoisturePin);
  int ldrValue = analogRead(ldrPin);
  int ntcValue = analogRead(ntcPin);

  // Depending on temperature sensor used, equation might change.
  float voltage = ntcValue * (5.0 / 1023.0);
  float temperatureC = (voltage - 0.5) * 100.0;

  Serial.print("Soil Moisture: ");
  Serial.print(soilMoistureValue);
  Serial.print(", LDR: ");
  Serial.print(ldrValue);
  Serial.print(", Temperature (C): ");
  Serial.println(temperatureC);

  delay(1000);
}
