#include <LiquidCrystal.h> 

int Contrast=75;
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);  
const int ledPin1 = 13; // the pin that the LED is attached to
const int ledPin2 = 10; // the pin that the LED is attached to
const int ledPin3 = 9; // the pin that the LED is attached to


void setup()
{
  // initialize serial communication:
  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(ledPin3, OUTPUT);
  
  analogWrite(6,Contrast);
  lcd.begin(16, 2);
} 
void loop()
{ 
  int status;
  int i;
  int text_len;
  String mystr;
  String text;
// see if there's incoming serial data:
  if (Serial.available() > 0) {
    text = Serial.readString();
    if (text.startsWith("1")){
      text = text.substring(1);
      text.trim();
      text_len = text.length();
      for(i =0;i<text_len;i++){
        if (text.charAt(i) == '1') {
          status = digitalRead(ledPin1);
          mystr = String(status);
          Serial.println(mystr);
          if (status == 1)
            digitalWrite(ledPin1, LOW);
          else
            digitalWrite(ledPin1, HIGH);
        }
        else if (text.charAt(i) == '2') {
          status = digitalRead(ledPin2);
          mystr = String(status);
          Serial.println(mystr);
          if (status == 1)
            digitalWrite(ledPin2, LOW);
          else
            digitalWrite(ledPin2, HIGH);
        }
        else if (text.charAt(i) == '3') {
          status = digitalRead(ledPin3);
          mystr = String(status);
          Serial.println(mystr);
          if (status == 1)
            digitalWrite(ledPin3, LOW);
          else
            digitalWrite(ledPin3, HIGH);
        }
      }

    }    
    if (text.startsWith("2")){
      lcd.setCursor(0, 0);
      text = text.substring(1);
      text.trim();
      lcd.print(text);
    }
    if (text.startsWith("3")){
      lcd.setCursor(0, 1);
      text = text.substring(1);
      text.trim();
      lcd.print(text);
    }
    if (text.startsWith("4")){
      lcd.clear();
    }
  }
}