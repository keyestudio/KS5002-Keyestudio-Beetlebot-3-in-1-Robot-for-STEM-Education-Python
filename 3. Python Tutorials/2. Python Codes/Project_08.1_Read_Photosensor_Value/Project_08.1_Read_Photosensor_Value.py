from machine import ADC, Pin
import time
# Initialize the photoresistance to pin 34 (ADC function)
adc = ADC(Pin(34))
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_10BIT)

# Print the current adc value of the photoresistance cyclically 
try:
    while True:
        adcValue = adc.read() # read the ADC value of photoresistance
        print("ADC Value:", adcValue) #Send the ADC value of photoresistance and print the result.
        time.sleep(0.5)
except:
    pass