import time
import os

# Scene Variables
sceneX = 50
sceneY = 67

# Rendering variables
fps = 60
framesFalling = 0

sceneArray = [

]
# Physics Varables
velocity = 1
accelaration = 9.81
initialHeight = 0

#Coeficient of restitution, value between 0 and 1
bounceElasticity = 0.95

# Ball Variables
class Position:
    def __init__(self, x, y):
        self.x = x  
        self.y = y
        
class Ball:
    def __init__(self):
        self.position = Position(5, initialHeight) # starting positon

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
    for i in range(sceneY+1):
         if i == sceneY:
             sceneRow = ['']*sceneX #row researved for deubug variables
             sceneArray.append(sceneRow)
         elif i == sceneY - 1:
             sceneRow = ['¯']*sceneX
             sceneArray.append(sceneRow)
         else:
             sceneRow = ['`']*sceneX
             sceneArray.append(sceneRow)

drawBlank()

# Runtime
while True:
#Physics 
#Ball Accelaration
    sceneArray[round(ball.position.y)][ball.position.x] = '`'

    positionUpdate = velocity + (accelaration/200) * framesFalling * framesFalling
    updatedPosition = ball.position.y + positionUpdate

        #Ground Check 
    if updatedPosition > sceneY - 2:
        ball.position.y = sceneY - 2
        framesFalling = 0
        velocity = -1*(bounceElasticity*velocity+1.9)
    else:
        ball.position.y = updatedPosition

    sceneArray[round(ball.position.y)][ball.position.x] = '@'
#Debug
    sceneArray[67][0] = updatedPosition #
#Ascii Rendering
    printScene()
    framesFalling += 1
    time.sleep(1/fps)