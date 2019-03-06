###### 1. Initialising the project #############################################

#### 1.1 Import libraries

import sys
sys.path.insert(1,'/home/pi/Go4Code/g4cSense/skeleton')

from sense_hat import SenseHat
from senselib import *
import random

#### 1.2 Initialisation

sense = SenseHat() # This will be used to control the the SenseHat.
initialise(sense) # Initialises the senselib library, that provides us with some useful functions
sense.clear() # Clears all pixels on the screen.

#### 1.3 Set up the variables

countdown = 10
number_colour = [0, 255, 0]

countdownMessage = "Time's up!"

###### 2. Set the countdown clock ##############################################

#### 2.1 Create a while-loop

selecting = True

while selecting:

    #### 2.2 Let the user choose the countdown time

    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "up":
                  countdown += 1
            elif event.direction == "down":
                countdown -= 1
            elif event.direction == "middle":
                selecting = False

    #### Bonus: Don't let the number go under 0 or over 99

    if countdown < 0:
        countdown += 100
    elif countdown > 99:
        countdown -= 100

    #### 2.3 Draw the current countdown time

    sense.clear()
    draw_two_digit_number(countdown, number_colour[0], number_colour[1], number_colour[2])

###### 3. Count down the time ##################################################

#### 3.1 Create a for-loop

for n in range(countdown, 0, -1):

    #### 3.2 Draw the countdown number

    sense.clear()
    draw_two_digit_number(n, number_colour[0], number_colour[1], number_colour[2])

    #### 3.3 Wait a second

    wait(1)

#### 4. Clock has finished #####################################################

sense.show_message(countdownMessage, 0.1)
