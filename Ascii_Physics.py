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
# Physics Varables
velocity = 1
accelaration = 9.81
initialHeight = 0

#Coeficient of restitution, value between 0 and 1
bounceElasticity = 0.9

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
#Ball Accelaration
    sceneArray[round(ball.position.y)][ball.position.x] = '`'
    #check if the ball is ABOUT to be set to a position past the scene boundaries (not currently written yet)
    ball.position.y += velocity + (accelaration/200) * currentFrame * currentFrame
        #Ground Check 
    if ball.position.y >= sceneY:
         ball.position.y = sceneY - 2
         currentFrame = 0
         velocity = -1*(bounceElasticity*velocity+3)

    ball.position.y = min(max(ball.position.y, 0), sceneY - 2)

    sceneArray[round(ball.position.y)][ball.position.x] = '@'
#Ascii Rendering
    printScene()
    currentFrame += 1
    time.sleep(1/fps)