import time
import os

# Scene Variables
sceneX = 50
sceneY = 25

sceneArray = [

]

# Ball Variables
class Position:
    def __init__(self, x, y):
        self.x = x  
        self.y = y
        
class Ball:
    def __init__(self):
        self.position = Position(0, 0) # starting positon

prevPositon = []

ball = Ball()
# Terminal Screen Control
    # clear terminal screen def
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
        sceneRow = ['`']*sceneX
        sceneArray.append(sceneRow)

drawBlank()

# Runtime
while True:
#Physics 
    sceneArray[ball.position.y][ball.position.x] = '@'

#Ascii Rendering
    printScene()
    time.sleep(0.1)