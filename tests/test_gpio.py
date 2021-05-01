from gpiozero import *
from time import sleep
from signal import pause
from ADCDevice import *

adc = ADS7830()
graphique = LEDBarGraph(22,6,13,26,16,12,5,25,24,23, initial_value=0, pwm=True)
buzzer = Buzzer(19)

graphique.value = 1
buzzer.beep(0.25, 0, 1)

def clampJoystick(val):
    if(val > 200): val = 1
    elif(val < 100): val = -1
    else: val = 0
    return -val

while True:
    valeurY = clampJoystick(adc.analogRead(1))
    valeurX = clampJoystick(adc.analogRead(0))
    
    
    print("X: " + str(valeurX) + " Y: " + str(valeurY))
    sleep(0.25)
