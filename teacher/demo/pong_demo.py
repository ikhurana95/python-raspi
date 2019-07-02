#### 1. Initialising the game ##################################################

#### 1.1 Import libraries

from sense_hat import SenseHat
from pong_lib import Pong
import random
from senselib import *

#### 1.2 Initialisation

sense = SenseHat() # This will be used to control the the SenseHat.
pong = Pong(sense) # Initializes the game.
initialise(sense) # Initialises the senselib library, that provides us with some useful functions

sense.clear() # Clears all pixels on the screen.
sense.show_message("PONG!", 0.03) # Display an intro message for the viewer.

#### 1.3 Set up the game variables

pong.player1size = 3 # Size of the player 1 paddle
pong.player1pos = 1 # Vertical position of the player 1 paddle
pong.player1colour = [0, 0, 255] # Colour of player 1 paddle
pong.player1score = 0 # Score of player 1

pong.player2size = 3 # Size of the player 2 paddle
pong.player2pos = 3 # Vertical position of the player 2 paddle
pong.player2colour = [255, 0, 0] # Colour of player 2 paddle
pong.player2score = 0 # Score of player 2

pong.ballX = 3 # Horizontal position of the ball
pong.ballY = 5 # Vertical position of the ball
pong.ballVelocityX = random.choice([-1, 1]) # Randomizes the vertical velocity of the ball.
pong.ballVelocityY = random.choice([-1, 1]) # Randomizes the horizontal velocity of the ball.
pong.ballColour = [0, 255, 0] # Colour of the ball

#### 2. Main game code #########################################################

while True:
    #### 2.1 Check for player1 movement (joystick)

    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "up":
                pong.player1pos -= 1
            elif event.direction == "down":
                pong.player1pos += 1

    #### 2.2 Let computer control player2

    pong.updatePlayer2()

    #### 2.3 Calculate new ball position

    newBallX = pong.ballX + pong.ballVelocityX
    newBallY = pong.ballY + pong.ballVelocityY

    #### 2.4 Check if new ball position has hit the player pads

    if newBallX == 0:
        if pong.ballY >= pong.player1pos and pong.ballY <= (pong.player1pos + pong.player1size):
            pong.ballVelocityX = -pong.ballVelocityX
            newBallX = pong.ballX + pong.ballVelocityX
            newBallY = pong.ballY + pong.ballVelocityY
    elif newBallX == 7:
        if pong.ballY >= pong.player2pos and pong.ballY <= (pong.player2pos + pong.player2size):
            pong.ballVelocityX = -pong.ballVelocityX
            newBallX = pong.ballX + pong.ballVelocityX
            newBallY = pong.ballY + pong.ballVelocityY

    #### 2.5 Check if new ball position is in goal

    if newBallX == -1: # Player 2 wins
        pong.player2score += 1
        newBallX = 3
        newBallY = 5
        sense.show_message(str(pong.player1score) + "-" + str(pong.player2score), 0.05)
    elif newBallX == 8: # Player 1 wins
        pong.player1score += 1
        newBallX = 3
        newBallY = 5
        sense.show_message(str(pong.player1score) + "-" + str(pong.player2score), 0.05)

    #### 2.6 Check if new ball position has collided with the top or bottom walls

    if newBallY == 0 or newBallY == 7:
        pong.ballVelocityY = -pong.ballVelocityY

    #### 2.7 Update ball position

    pong.ballX = newBallX
    pong.ballY = newBallY

    #### 2.8 Clear screen

    sense.clear()

    #### 2.9 Draw player1 and player2

    drawVerticalLine(0, pong.player1pos, pong.player1size, pong.player1colour[0], pong.player1colour[1], pong.player1colour[2])
    drawVerticalLine(7, pong.player2pos, pong.player2size, pong.player2colour[0], pong.player2colour[1], pong.player2colour[2])

    #### 2.10 Draw ball

    sense.set_pixel(pong.ballX, pong.ballY, pong.ballColour[0], pong.ballColour[1], pong.ballColour[2])

    #### 2.11 Wait a little bit before the next frame

    wait(0.5)
