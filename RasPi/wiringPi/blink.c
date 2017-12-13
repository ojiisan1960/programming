#include <wiringPi.h>
#define LED 7

int main(void){
	wiringPiSetup();
	pinMode (LED, OUTPUT);
	for(;;)
	{
	digitalWrite(LED,HIGH);
	delay(500);
	digitalWrite(LED,LOW);
	delay(500);
	}
	return 0; 
}
