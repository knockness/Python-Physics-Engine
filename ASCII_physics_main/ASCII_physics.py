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

scene.drawBlank()

# Runtime
while True:
#Physics 
        #Ball Accelaration
    scene.sceneArray[ball.position.x, round(ball.position.y)] = '`'

    positionUpdate = velocity + (accelaration/200) * framesFalling * framesFalling
    updatedPosition = ball.position.y - positionUpdate

        #Ground Check 
    if updatedPosition < 1:
        ball.position.y = 1
        framesFalling = 0
        velocity = -1*(objects.ball.bounceElasticity*velocity+1.9)
    else:
        ball.position.y = updatedPosition

    scene.sceneArray[ball.position.x, round(ball.position.y)] = '@'
        #Debug
    scene.sceneArray[0, -1] = updatedPosition
        #Ascii Rendering
    scene.printScene()
    framesFalling += 1
    time.sleep(1/fps)