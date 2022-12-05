


# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import sys
sys.path.insert(1, 'lcd/')
import drivers

class Servo:
    def __init__(self, pin):
        
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin,GPIO.OUT)
        self.p = GPIO.PWM(pin,50) # PIN 18 PWM 
        self.p.start(self.duty(15))
        time.sleep(1)

    def duty(self,aci): 
        return (float(aci) / 18.0 + 2)
    
    
    def servo(self,aci):
        
        self.p.ChangeDutyCycle(self.duty(aci))
        time.sleep(2)              
        self.p.stop()
        GPIO.cleanup()
        time.sleep(1)

class Lcd:
  
    import time    

    def __init__(self):
        self.display = drivers.Lcd() 
    

    def lcd(self,message,message2,showtime):
        self.display.lcd_backlight(1)  
        self.display.lcd_display_string(message, 1)
        self.display.lcd_display_string(message2, 2)
        time.sleep(showtime)
        self.display.lcd_clear()
        self.display.lcd_backlight(0)
   
if __name__ == "__main__":
    lcd = Lcd()
    lcd.lcd("  Yasiyosun","    Bu Hayati",5)
   
   
    
        
     