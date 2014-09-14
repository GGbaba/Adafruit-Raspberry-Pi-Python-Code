#!/usr/bin/python

from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from subprocess import call
from subprocess import Popen

def run_cmd(cmd): 
   p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) 
   output = p.communicate()[0] 
   return output
   
# Initialize the LCD plate.  Should auto-detect correct I2C bus.  If not,
# pass '0' for early 256 MB Model B boards or '1' for all later versions
lcd = Adafruit_CharLCDPlate()

# Clear display and show greeting, pause 1 sec
lcd.backlight(0)
lcd.clear()
#lcd.message("Adafruit RGB LCD\nPlate w/Keypad!")
sleep(1)
lcd.backlight(1)

# Cycle through backlight colors
#col = (lcd.RED , lcd.YELLOW, lcd.GREEN, lcd.TEAL,
#       lcd.BLUE, lcd.VIOLET, lcd.ON   , lcd.OFF)
#for c in col:
#    lcd.backlight(c)
#    sleep(.5)

# Poll buttons, display message & set backlight accordingly
btn = ((lcd.SELECT, 'mpc'                       , lcd.ON),
       (lcd.LEFT  , 'shairport'                 , lcd.RED),
       (lcd.UP    , 'Sita sings\nthe blues'     , lcd.BLUE),
       (lcd.DOWN  , 'I see fields\nof green'    , lcd.GREEN),
       (lcd.RIGHT , 'Purple mountain\nmajesties', lcd.VIOLET))
       
prev = -1
a=0
c=-1
while True:
    for b in btn:
        if lcd.buttonPressed(b[0]):
               #if lcd.message(b[1]) == "mpc":
               if b[0] == 0 :
                     if a is 0 :
                            #call(["mpcgg", "play"])
                            #lcd.message("mpc !!!")
                            lcd.message(run_cmd("mpcgg play"))
                            print'mpc !!!'
                            a=1
                     else :
                            lcd.message(run_cmd("mpcgg stop"))
                            print'mpc !!!'
                            #call(["mpcgg", "stop"])
                            #lcd.message("mpc !!!")
                            a=0
               #if lcd.message(b[1]) is 'shairport':
               if b[0] == 1 :
                     call(["shairport", "&"])
                     lcd.message("shairport !!!")
                     print'shairport !!!'
               if b[0] == 2 :
                     if c is 0 : 
                            lcd.backlight(1)
                     else :
                            lcd.backlight(0)
                            c=0
               sleep(.2)
               break
               '''
            if b is not prev:
                call(["mpcgg", "play"])
                call(["ls", "-l"])
                lcd.clear()
                lcd.message(b[1])
                #lcd.backlight(b[2])
                prev = b
            break
            '''
