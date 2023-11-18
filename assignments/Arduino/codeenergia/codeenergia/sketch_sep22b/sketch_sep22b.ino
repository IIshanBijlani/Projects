
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 16, 2);
void setup() {
  lcd.begin(16, 2);
  lcd.init();
  lcd.backlight();
 
}
void loop() {
  lcd.setCursor(0, 0);
  lcd.print("Saksham Digital");
  delay(1000);

  lcd.setCursor(0, 1);
  lcd.print("Voltage: 1.3");
  delay(20000);

  lcd.clear();

  lcd.setCursor(0, 0);
  lcd.print("Saksham Digital");
  delay(1000);

  
  lcd.setCursor(0, 1);
  lcd.print("Voltage: 1.5");
  delay(30000);

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Saksham Digital");
  delay(1000);
  
  lcd.setCursor(0, 1);
  lcd.print("Voltage: 1.7");
  delay(20000);

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Saksham Digital");
  delay(1000);
  
  lcd.setCursor(0, 1);
  lcd.print("Voltage: 1.5");
  delay(30000);

  lcd.clear();
  

  lcd.setCursor(0, 0);
  lcd.print("Saksham Digital");
  delay(1000);
  
  lcd.setCursor(0, 1);
  lcd.print("Voltage: 1.7");
  delay(20000);

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Saksham Digital");
  delay(1000);
  
  lcd.setCursor(0, 1);
  lcd.print("Voltage: 1.9");
  delay(30000);

 
  
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Saksham Digital");
  delay(1000);
  
  lcd.setCursor(0, 1);
  lcd.print("Voltage: 2.0");
  delay(20000);

  
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Saksham Digital");
  delay(1000);
  
  lcd.setCursor(0, 1);
  lcd.print("Voltage: 1.9");
  delay(30000);

;
  
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Saksham Digital");
  delay(1000);
  
  lcd.setCursor(0, 1);
  lcd.print("Voltage: 2.0");
  delay(2000);


  
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Saksham Digital");
  delay(1000);
  
  lcd.setCursor(0, 1);
  lcd.print("Voltage: 2.2");
  delay(30000);
  
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Saksham Digital");
  delay(1000);
  
  lcd.setCursor(0, 1);
  lcd.print("Voltage: 2.1");
  delay(20000);
  
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Saksham Digital");
  delay(1000);
  
  lcd.setCursor(0, 1);
  lcd.print("Voltage: 2.3");
  delay(30000);

  lcd.clear();
   
}
