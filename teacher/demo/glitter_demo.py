# Import libraries

from sense_hat import SenseHat
from senseGraphics import *
import random
import time

# (1.2) Initialisation

sense = SenseHat() # This will be used to control the the SenseHat.
initialise(sense) # Initialises the senselib library, that provides us with some useful functions
sense.set_imu_config(True, True, True)
sense.clear() # Clears all pixels on the screen.


## 2.0 Available colours

colours = [
  "yellow","blue", "red","pink","green","orange", "violet","purple","gold"
  ]


## 2.1 set the colour of glitter
glitter_colour =random.choice(colours) ##This doesn't have to be a random choice

while True:


  ## 2.2 creating an empty list that will hold the image
  image = []

  for i in range(64):

    ## 2.3 get a random shade of some colour
    shade = randomShade(glitter_colour)

    ## 2.4 add that to your list
    image.append(shade)


   ## 2.5 Set the pixels to show the image
  sense.set_pixels(image)

  ## Make the Raspberry Pi sleep for a bit
  time.sleep(0.1)

####Bonus section is only needed if students are implementing the bonus feautre ####

  ## Bonus: Change colour by shake

  ac = sense.get_accelerometer_raw()
  x = ac["x"]
  y = ac["y"]
  z = ac["z"]
  shake = x*x + y*y + z*z
  if shake > 5.0:

      glitter_colour = random.choice(colours)
