import utime as time
from machine import I2C, Pin, RTC, PWM 
from ht16k33matrix import HT16K33Matrix

#Define GPIO4’s output frequency as 50Hz and its duty cycle as 77, and assign them to PWM.
servoPin = Pin(4)
pwm = PWM(servoPin, freq=50)
pwm.duty(77)
time.sleep(1)

#Set the pin and sound speed of the ultrasonic sensor.
trigPin=Pin(5,Pin.OUT,0)
echoPin=Pin(18,Pin.IN,0)
soundVelocity=340
distance=0
# right wheel
pin1=Pin(32,Pin.OUT)
pin2=PWM(Pin(25),freq=50,duty=0)
# left wheel
pin3=Pin(33,Pin.OUT)
pin4=PWM(Pin(26),freq=50,duty=0)

# As a function of the car going forward.
def car_forward():
  pin1.value(0)
  pin2.duty(200) 
  pin3.value(0)
  pin4.duty(250)  

# As a function of the car going left.
def car_left():
  pin1.value(0)
  pin2.duty(500) 
  pin3.value(1)
  pin4.duty(500)  

# As a function of the car going right.
def car_right():
  pin1.value(1)
  pin2.duty(500) 
  pin3.value(0)
  pin4.duty(500)

# As a function of the car stopping.
def car_stop():
  pin2.deinit()
  pin4.deinit()
  pin1.value(0)
  pin2.duty(0) 
  pin3.value(0)
  pin4.duty(0)
  
  
#Subfunction getSonar() is used to start the Ultrasonic Module to begin measurements,
#and return the measured distance in centimeters. In this function, first let trigPin
#send 10us high level to start the Ultrasonic Module. Then use pulseIn() to read
#the Ultrasonic Module and return the duration time of high level.
#Finally, the measured distance according to the time is calculated.  
def getSonar(): 
    trigPin.value(1)
    time.sleep_us(10)
    trigPin.value(0)
    while not echoPin.value():
        pass
    pingStart=time.ticks_us()
    while echoPin.value():
        pass
    pingStop=time.ticks_us()
    pingTime=time.ticks_diff(pingStop,pingStart)
    distance=pingTime*soundVelocity//2//10000
    time.sleep_ms(10)
    return int(distance)

# CONSTANTS
DELAY = 0.01
PAUSE = 3
# START
if __name__ == '__main__':
    i2c = I2C(scl=Pin(22), sda=Pin(21))
    display = HT16K33Matrix(i2c)
    display.set_brightness(2)

while True:
    Distance=getSonar() #Get the distance measured by ultrasound.
    if Distance>0 and Distance<10: #If the distance is greater than 0, it's less than 10.
        car_stop() # Car stop
        # Draw a custom icon on the LED
        icon = b"\x18\x18\x18\x18\x18\x00\x00\x18"
        display.set_icon(icon).draw()
        # Rotate the icon
        display.set_angle(0).draw()
        time.sleep(0.2)
        pwm = PWM(servoPin, freq=50)
        pwm.duty(128)
        time.sleep(0.3)
        a1=getSonar()
        time.sleep(0.2)
        pwm = PWM(servoPin, freq=50)
        pwm.duty(25)
        time.sleep(0.3)
        a2=getSonar()
        time.sleep(0.2)
        if a1>a2:
            pin2=PWM(Pin(25),freq=50)
            pin4=PWM(Pin(26),freq=50)
            car_left()
            icon = b"\x48\x24\x12\x09\x09\x12\x24\x48"
            display.set_icon(icon).draw()
            display.set_angle(0).draw()
            pwm = PWM(servoPin, freq=50)
            pwm.duty(77)
            time.sleep(0.3)
            icon = b"\x18\x24\x42\x99\x24\x42\x81\x00"
            display.set_icon(icon).draw()
            display.set_angle(0).draw()
        else:
            pin2=PWM(Pin(25),freq=50)
            pin4=PWM(Pin(26),freq=50)
            car_right()
            icon = b"\x12\x24\x48\x90\x90\x48\x24\x12"
            display.set_icon(icon).draw()
            # Rotate the icon
            display.set_angle(0).draw()
            pwm = PWM(servoPin, freq=50)
            pwm.duty(77)
            time.sleep(0.3)
            icon = b"\x18\x24\x42\x99\x24\x42\x81\x00"
            display.set_icon(icon).draw()
            display.set_angle(0).draw()
    else:
        pin2=PWM(Pin(25),freq=50)
        pin4=PWM(Pin(26),freq=50)
        car_forward() #Car ahead
        icon = b"\x18\x24\x42\x99\x24\x42\x81\x00"
        display.set_icon(icon).draw()
        display.set_angle(0).draw()