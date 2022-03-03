from m5stack import *
from m5stack_ui import *
from uiflow import *
import time

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)



i = 1
j = 1

while True:
  rgb.setColor((i%10)+1, 0xff0000)                #color of the first LED
  rgb.setColor(((i+1)%10)+1, 0x0000ff)            #color of the 2nd LED
  rgb.setColor(((i+2)%10)+1, 0x000000)            #color removal
  rgb.setColor(((i-1)%10)+1, 0x000000)            #color removal
  rgb.setColor(((i+5)%10)+1, 0xff0000)            #color of the first LED of the other side
  rgb.setColor(((i+6)%10)+1, 0x0000ff)            #color of the 2nd LED of the other side
  rgb.setColor(((i+7)%10)+1, 0x000000)            #color removal
  rgb.setColor(((i+4)%10)+1, 0x000000)            #color removal

                #color control of each LED:
#  rgb.setColor((i%10)+1, 0xff6666)
#  rgb.setColor(((i+1)%10+1, 0xff2222)
#  rgb.setColor(((i+2)%10)+1, 0xff0000)
#  rgb.setColor(((i+3)%10)+1, 0x66ff66)
#  rgb.setColor(((i+4)%10)+1, 0x22ff22)
#  rgb.setColor(((i+5)%10)+1, 0x00ff00)
#  rgb.setColor(((i+6)%10)+1, 0x6666ff)
#  rgb.setColor(((i+7)%10)+1, 0x2222ff)
#  rgb.setColor(((i+8)%10)+1, 0x0000ff)
#  rgb.setColor(((i+9)%10)+1, 0x000000)
  
  i += 1 * j                                      #to keep turning in one direction, remove everything after "i += 1" except "wait(0.05)"
  
  if i%(3+5*x)==0: # x - number of repetitions of the cycles, 0 = standard ; by changing the number of LEDs at a time, the length of the cycle changes 2 LEDs = i%(3+5*x), 1 LED = i%(4+5*x)
    j *= -1
    
  wait(0.05)