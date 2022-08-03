import requests
import sys
import time
import pytz
from datetime import datetime
from pytz import timezone
from tcp_client import client_fun


sys.path.append('/home/pi/Dexter/GrovePi/Software/Python')

import grovepi
import grove_rgb_lcd as lcd

# Modules for my apps
import nomics

#Port init
PORT_BUZZER = 2             # D2
PORT_BUTTON = 8             # D8
PORT_RED_BUTTON = 3         # D3
PORT_GREEN_BUTTON = 4       # D4

LCD_LINE_LEN = 16

# Setup
grovepi.pinMode(PORT_BUZZER, "OUTPUT")
grovepi.pinMode(PORT_GREEN_BUTTON, "INPUT")
grovepi.pinMode(PORT_RED_BUTTON, "INPUT")

#set lcd color
lcd.setRGB(255, 255, 255)

# Installed Apps!
APPS = [
    nomics.BITCOIN_APP
]

# Cache to store values so we save time and don't abuse the APIs
CACHE = [''] * len(APPS)
for i in range(len(APPS)):
    # Includes a two space offset so that the scrolling works better
    CACHE[i] = '  ' + APPS[i]['init']()

app = 0     # Active app
ind = 0     # Output index

#get initial price before starting
init_price = float(CACHE[app][ind:ind+LCD_LINE_LEN])
init_price = round(init_price, 2)
#get initial time before starting
date_format ='%H:%M:%S %Z'
first_date = datetime.now(tz=pytz.utc)
first_date = first_date.astimezone(timezone('US/Pacific'))
test = str(first_date)
#creating a dictionary to keep track of pairs
main_dict = {}
main_dict[test[11:19]] = init_price

while True:
    try:

        if(len(main_dict) == 10):
            #using tcp client to send data to server to process
            #print link to trend line in terminal
            client_fun(main_dict)
            #clear main_dict
            main_dict.clear()
        
        if grovepi.digitalRead(PORT_BUTTON):
            #make a new call to API to get updated price
            APPS = [ nomics.BITCOIN_APP ] 
            # Cache to store values so we save time and don't abuse the APIs
            CACHE = [''] * len(APPS)
            for i in range(len(APPS)):
                # Includes a two space offset so that the scrolling works better
                CACHE[i] = '  ' + APPS[i]['init']()
            #collect new price
            updated_price = float(CACHE[app][ind:ind+LCD_LINE_LEN])
            updated_price = round(updated_price, 2)
            #collect new time
            innertemp = datetime.now(tz=pytz.utc)
            innertemp = innertemp.astimezone(timezone('US/Pacific'))
            tme = str(innertemp)
            #add time,price to dict
            main_dict[tme[11:19]] = updated_price
            time.sleep(1)

            #hit the lights code
            #if no change has occured turn on both LEDs
            if(updated_price == init_price):
                #turn on green and red
                grovepi.digitalWrite(PORT_GREEN_BUTTON, 1)
                grovepi.digitalWrite(PORT_RED_BUTTON, 1)
                #recovery period (meant to prevent overloading api requests)
                time.sleep(1)
                #turn off green and red
                grovepi.digitalWrite(PORT_RED_BUTTON, 0)
                grovepi.digitalWrite(PORT_GREEN_BUTTON, 0)
            #the price has increased
            elif(updated_price > init_price):
                #update price
                init_price = updated_price
                #turn on light and buzzer
                grovepi.digitalWrite(PORT_GREEN_BUTTON, 1)
                grovepi.digitalWrite(PORT_BUZZER, 1)
                #recovery period (meant to prevent overloading api requests)
                time.sleep(1)
                #turn off light and buzzer
                grovepi.digitalWrite(PORT_BUZZER, 0)
                grovepi.digitalWrite(PORT_GREEN_BUTTON, 0)
            #the price has decreased
            elif(updated_price < init_price):
                #update price
                init_price = updated_price
                #turn on light and buzzer
                grovepi.digitalWrite(PORT_RED_BUTTON, 1)
                grovepi.digitalWrite(PORT_BUZZER, 1)
                #recovery period (meant to prevent overloading api requests)
                time.sleep(1)
                #turn off light and buzzer
                grovepi.digitalWrite(PORT_BUZZER, 0)
                grovepi.digitalWrite(PORT_RED_BUTTON, 0)
        
        #Display Output
        lcd.setText_norefresh(APPS[app]['name'] + '\n' + '$' + str(init_price))

    except KeyboardInterrupt:
        # Gracefully shutdown on Ctrl-C
        lcd.setText('')
        lcd.setRGB(0, 0, 0)

        # Turn buzzer off just in case
        grovepi.digitalWrite(PORT_BUZZER, 0)

        break

    except IOError as ioe:
        if str(ioe) == '121':
            # Retry after LCD error
            time.sleep(0.25)

        else:
            raise
