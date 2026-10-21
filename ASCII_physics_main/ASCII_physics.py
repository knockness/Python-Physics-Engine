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

prevPositon = []

ball = objects.ball.ball

myScene = scene.createScene(50, 67)

# Runtime
while True:
#Physics 
        #Ball Accelaration
    myScene[ball.position.x, round(ball.position.y)] = '`'

    positionUpdate = velocity + (accelaration/200) * framesFalling * framesFalling
    updatedPosition = ball.position.y - positionUpdate

        #Ground Check 
    if updatedPosition < 1:
        ball.position.y = 1
        framesFalling = 0
        velocity = -1*(objects.ball.bounceElasticity*velocity+1.9)
    else:
        ball.position.y = updatedPosition

    myScene[ball.position.x, round(ball.position.y)] = '@'
        #Debug
    myScene[0, -1] = updatedPosition
        #Ascii Rendering
    scene.printScene(myScene)
    framesFalling += 1
    time.sleep(1/fps)