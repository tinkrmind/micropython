############# Hello World! ########################
from microbit import *

display.scroll("Hello, World!")

############### Display an Image ########################
from microbit import *

display.show(Image.HAPPY)

################### Touch #################
from microbit import *

while True:
    if pin0.is_touched():
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)

################### Digital Write ################
from microbit import *

while True:
    pin0.write_digital(1)
    sleep(20)
    pin0.write_digital(0)
    sleep(20)

################## Music ####################
import music

music.play(music.NYAN)
music.pitch(2500, 10)

############## Random ####################
from microbit import *

import random
display.show(str(random.randint(1, 6)))

############# Accelerometer ############
from microbit import *

while True:
    reading = accelerometer.get_x()
    if reading > 20:
        display.show("R")
    elif reading < -20:
        display.show("L")
    else:
        display.show("-")

################FILES##################
from microbit import *

with hello.txt as myfile:
    myfile.write("Hello, world!")

############## Radio Signal ################
from microbit import *
import radio

radio.on()

while True:
    rec = radio.receive()
    if rec != None:
        print(rec)
    if rec == 'amitabh':
        display.show(Image.HEART, 100)
        sleep(1000)
        display.clear()
        radio.send('david')

############# Radio Send ##############
from microbit import *
import radio

radio.on()

while True:
    rec = radio.receive()
    if rec != None:
        print(rec)

    if button_a.get_presses() > 0:
        radio.send('amitabh')
