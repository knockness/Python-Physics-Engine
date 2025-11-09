import math
import time
import os

# Scene Variables
sceneX = 50
sceneY = 67

# Rendering variables
fps = 60
currentFrame = 0

sceneArray = [

]

# Ball Variables
class Position:
    def __init__(self, x, y):
        self.x = x  
        self.y = y

class Ball:
    def __init__(self):
        self.position = Position(5, 0) # starting positon

prevPositon = []

ball = Ball()
# Terminal Screen Control
    # clear terminal screen def
    #clear function only works on debug from terminal -> it does not work on intelliJ's virtual environment
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

    # Print Written Scene
def printScene():
    clear()
    for sublist in sceneArray:
        print(" ".join(map(str, sublist)))

# Scene Writing
    # draw blank screen def
def drawBlank():
    clear()
    for i in range(sceneY):
        if i == sceneY-1:
            sceneRow = ['¯']*sceneX
            sceneArray.append(sceneRow)
        else:
            sceneRow = ['`']*sceneX
            sceneArray.append(sceneRow)

drawBlank()

# Runtime
while True:

#Physics 
    sceneArray[math.floor(ball.position.y)][ball.position.x] = '`'
    ball.position.y = 0.5*(9.81/100)*(currentFrame*currentFrame)
    sceneArray[math.floor(ball.position.y)][ball.position.x] = '@'

#Ascii Rendering
    printScene()
    currentFrame += 1
    time.sleep(1/fps)