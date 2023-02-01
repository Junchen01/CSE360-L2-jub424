import time
from Motor import *
from Led import *
from Buzzer import *

# The left side motor have more power
# under this situation it go stright line 
def forward_2():
    PWM.setMotorModel(500,500,1000,1000)
    time.sleep(2)

# Turn left for 0.6s and stop, app. 90 degree
def left_90():
    PWM.setMotorModel(-1500,-1500,2000,2000)
    time.sleep(0.60)
    PWM.setMotorModel(0,0,0,0)

# the light for this car(id:12) is (B,G,R)
def light_led(led_id,b,g,r):
    led.ledIndex(led_id,b,g,r)

# beep for 1s and then stop
def beep():
    buzzer=Buzzer()
    buzzer.run('1')
    time.sleep(1)
    buzzer.run('0')

#sleep for 2s and then start
# move forward 2s
forward_2()
# 90 degrees
left_90()
# LED 0 red
light_led(0x01,0,255,0)
# move forward 2s
forward_2()
# 90 degrees
left_90()
# LED 1 blue
light_led(0x02,0,0,255)
# move forward 2s
forward_2()
# 90 degrees
left_90()
# LED 2 green
light_led(0x04,255,0,0)
# move forward 2s
forward_2()
# 90 degrees
left_90()
# LED 3 yellow
light_led(0x08,255,255,0)
# beep
beep()

# turn off light and motor
PWM.setMotorModel(0,0,0,0)
led.colorWipe(led.strip, Color(0,0,0))

