from machine import Pin,PWM
import time

# right wheel
pin1=Pin(32,Pin.OUT)
pin2=PWM(Pin(25),freq=12500)

# left wheel
pin3=Pin(33,Pin.OUT)
pin4=PWM(Pin(26),freq=12500)

# As a function of the car going forward.
def car_forward(): 
  pin1.value(0)
  pin2.duty(1000) 
  pin3.value(0)
  pin4.duty(1000)  

# As a function of the car going backwards.
def car_back(): 
  pin1.value(1)
  pin2.duty(250) 
  pin3.value(1)
  pin4.duty(250)

# As a function of the car going left.
def car_left(): 
  pin1.value(0)
  pin2.duty(1000) 
  pin3.value(1)
  pin4.duty(500)  

# As a function of the car going right.
def car_right(): 
  pin1.value(1)
  pin2.duty(500) 
  pin3.value(0)
  pin4.duty(1000)

# As a function of the car stopping.
def car_stop(): 
  pin1.value(0)
  pin2.duty(0) 
  pin3.value(0)
  pin4.duty(0)   
try:
    while True:
        car_forward() #Car ahead
        time.sleep(2) # delay 2s
        car_back() # Car goes back
        time.sleep(2)    
        car_left() # Car to the left
        time.sleep(2)    
        car_right() # Car to the right
        time.sleep(2)    
        car_stop() # Car stop
        time.sleep(2)     
except:
    pass