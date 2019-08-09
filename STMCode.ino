#define tempSensorPin PA2
#define soilHumiditySensorPin PA1
#define lightIntensitySensorPin PA0
void getSoilHumidity() {
String string3 = String("S");
string3+=analogRead(soilHumiditySensorPin);
Serial.println(string3);
}
void getTemperature() {
String string2 = String("T");
string2+=analogRead(tempSensorPin);
Serial.println(string2);
}
void getLightIntensity() {
String string1 = String("L");
string1+=analogRead(lightIntensitySensorPin);
Serial.println(string1);
}
void setup() {
  // put your setup code here, to run once:
Serial.begin(115200);
pinMode(tempSensorPin,INPUT);
pinMode(soilHumiditySensorPin,INPUT);
pinMode(lightIntensitySensorPin,INPUT);
Serial.flush();
}

void loop() {
  // put your main code here, to run repeatedly:
String string3 = String("S");
string3+=analogRead(soilHumiditySensorPin);
String string1 = String("L");
string1+=analogRead(lightIntensitySensorPin);
String string2 = String("T");
string2+=analogRead(tempSensorPin);
String fin=String(string1+","+string2+","+string3);
Serial.println(fin);
delay(300);
}
