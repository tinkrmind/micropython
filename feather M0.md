## Installing board definitions

* Install [Arduino IDE](https://www.arduino.cc/en/Main/Software)
* Open Arduino, and click File > Preferences. To the right of the Additional Boards Manager URLs, click on the Additional URLs window button.
* Add https://adafruit.github.io/arduino-board-index/package_adafruit_index.json to the list
* Go to Tools > Boards > Board manager and search adafruit
* Install Adafruit SAMD boards

## Installing UF2 bootloader

* Download [this .ino file](https://github.com/adafruit/uf2-samdx1/releases/download/v3.6.0/update-bootloader-feather_m0-v3.6.0.ino) from this repo and open it in Arduino
* Choose Tools> Board > Adafruit M0 basic
* Choose the right port
* Upload!
* You should see a new USB drive named FEATHERBOOT

## Installing circuit python

* Download .uf2 file from [here](https://circuitpython.org/board/feather_m0_basic/)
* Drag and drop the file to the FEATHERBOOT drive
* FEATHERBOOT drive should get ejected and a new drive named CIRCUITPY should appear

## Test it!

* Open atom or similar text editor
* Copy paste the following code:
<pre><code>
import board
import digitalio
import time
pin_name = board.D13
led = digitalio.DigitalInOut(pin_name)
led.direction = digitalio.Direction.OUTPUT
while True:
    led.value = True
    time.sleep(0.1)
    led.value = False
    time.sleep(0.1)
    </code></pre>
    
## Install Mu

* Install Mu from [here](https://codewith.mu/en/download)
