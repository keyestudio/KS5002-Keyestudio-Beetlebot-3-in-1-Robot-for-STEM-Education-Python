from machine import Pin, ADC, PWM
import time

#Define GPIO4’s output frequency as 50Hz and its duty cycle as 77, and assign them to PWM.
servoPin = Pin(4)
pwm = PWM(servoPin, freq=50)
pwm.duty(77)
time.sleep(1)

# Initialize the left photoresistance to pin 34 (ADC function)
adc1 = ADC(Pin(34))
adc1.atten(ADC.ATTN_11DB)
adc1.width(ADC.WIDTH_10BIT)
# Initialize the right photoresistance to pin 35 (ADC function)
adc2 = ADC(Pin(35))
adc2.atten(ADC.ATTN_11DB)
adc2.width(ADC.WIDTH_10BIT)

# right wheel
pin1=Pin(32,Pin.OUT)
pin2=PWM(Pin(25),freq=50,duty=0)
# left wheel
pin3=Pin(33,Pin.OUT)
pin4=PWM(Pin(26),freq=50,duty=0)

# As a function of the car going forward.
def car_forward(): 
  pin1.value(0)
  pin2.duty(300) 
  pin3.value(0)
  pin4.duty(300)  

# As a function of the car going backwards.
def car_back(): 
  pin1.value(1)
  pin2.duty(200) 
  pin3.value(1)
  pin4.duty(200)

# As a function of the car going left.
def car_left(): 
  pin1.value(0)
  pin2.duty(200) 
  pin3.value(1)
  pin4.duty(900)  

# As a function of the car going right.
def car_right(): 
  pin1.value(1)
  pin2.duty(900) 
  pin3.value(0)
  pin4.duty(200)

# As a function of the car stopping.
def car_stop():
  pin2.deinit()
  pin4.deinit() 
  pin1.value(0)
  pin2.duty(0) 
  pin3.value(0)
  pin4.duty(0)   

while True:
    adcValue1 = adc1.read() # read the ADC value of the left photoresistance.
    adcValue2 = adc2.read() # read the ADC value of the right photoresistance.
    print("ADC Value1:", adcValue1 ,"ADC Value2:", adcValue2)
    time.sleep(0.5)
    if adcValue1 > 700 and adcValue2 > 700: #Range values measured by left and right photoresistances.
        pin2=PWM(Pin(25),freq=50)
        pin4=PWM(Pin(26),freq=50)
        car_forward() #Car ahead
    elif adcValue1 > 700 and adcValue2 <= 700:
        pin2=PWM(Pin(25),freq=50)
        pin4=PWM(Pin(26),freq=50) 
        car_left()
    elif adcValue1 <= 700 and adcValue2 > 700:
        pin2=PWM(Pin(25),freq=50)
        pin4=PWM(Pin(26),freq=50)
        car_right()
    else:
        car_stop()