# Default Python Imports
import time
import os

# Project Imports
import objects
import scene

# Rendering variables
fps = 60
framesFalling = 0

# Physics Varables
velocity = 1
accelaration = 9.81

#Coeficient of restitution, value between 0 and 1
bounceElasticity = 0.95
prevPositon = []

ball = objects.Ball()

scene.drawBlank()

# Runtime
while True:
#Physics 
#Ball Accelaration
    scene.sceneArray[round(ball.position.y)][ball.position.x] = '`'

    positionUpdate = velocity + (accelaration/200) * framesFalling * framesFalling
    updatedPosition = ball.position.y + positionUpdate

        #Ground Check 
    if updatedPosition > scene.sceneY - 2:
        ball.position.y = scene.sceneY - 2
        framesFalling = 0
        velocity = -1*(bounceElasticity*velocity+1.9)
    else:
        ball.position.y = updatedPosition

    scene.sceneArray[round(ball.position.y)][ball.position.x] = '@'
#Debug
    scene.sceneArray[67][0] = updatedPosition #
#Ascii Rendering
    scene.printScene()
    framesFalling += 1
    time.sleep(1/fps)