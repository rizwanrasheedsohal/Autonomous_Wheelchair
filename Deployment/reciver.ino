#include <SoftwareSerial.h>


void setup(){


 Serial.begin(9600);
 Serial.println("Starting XBee Comunication");
 pinMode(6, OUTPUT);
 pinMode(7, OUTPUT);
 pinMode(8, OUTPUT);
 pinMode(9, OUTPUT);

 
}


void loop(){
 char tmp=Serial.read();
if(tmp=='f'){
  Serial.print(tmp);
  digitalWrite(6, HIGH);
  digitalWrite(7, LOW);
  digitalWrite(8, LOW);
  digitalWrite(9, HIGH);// sets the digital pin 13 on
 
 }
 if(tmp=='s'){
  Serial.print(tmp);
  digitalWrite(6, LOW);
  digitalWrite(9, LOW);
   digitalWrite(7, LOW);
  digitalWrite(8, LOW);
  // sets the digital pin 13 off
 }  

 if(tmp=='l'){
  Serial.print(tmp);
  digitalWrite(6, HIGH);
  digitalWrite(7, LOW);
  digitalWrite(8, HIGH);
  digitalWrite(9, LOW);// sets the digital pin 13 on
 
 }
 
 if(tmp=='r'){
  Serial.print(tmp);
  digitalWrite(6, LOW);
  digitalWrite(7, HIGH);
  digitalWrite(8, LOW);
  digitalWrite(9, HIGH);// sets the digital pin 13 on
 
 }

 if(tmp=='b'){
  Serial.print(tmp);
  digitalWrite(6, LOW);
  digitalWrite(7, HIGH);
  digitalWrite(8, HIGH);
  digitalWrite(9, LOW);// sets the digital pin 13 on
 
 }
 
 
}
