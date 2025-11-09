import math
import random
import time
import os

# Scene Variables
sceneX = 160
sceneY = 80
fps = 60
currentFrame = 0

sceneArray = []

# Ball Variables
class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Ball:
    def __init__(self):
        self.position = Position(5, 5)
        angle = random.randint(20, 70)
        speed = random.randint(1, 3) #init velocity
        self.vx = speed * math.cos(math.radians(angle))
        self.vy = speed * math.sin(math.radians(angle))

ball = Ball()

# clear terminal screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# print scene
def printScene():
    clear()
    for sublist in sceneArray:
        print("".join(map(str, sublist)))

# draw blank scene
def drawBlank():
    sceneArray.clear()
    for i in range(sceneY):
        if i == sceneY - 1:
            sceneRow = ['¯'] * sceneX
        else:
            sceneRow = ['`'] * sceneX
            #this can be changed to ' ' instead
        sceneArray.append(sceneRow)

# Runtime
gravity = -0.05

while True:
    drawBlank()

    ball.vy += gravity
    ball.position.x += ball.vx
    ball.position.y -= ball.vy

    if ball.position.x <= 0:
        ball.position.x = 0
        ball.vx *= -1
    elif ball.position.x >= sceneX - 1:
        ball.position.x = sceneX - 1
        ball.vx *= -1

    if ball.position.y >= sceneY - 2:
        ball.position.y = sceneY - 2
        ball.vy *= -0.8 # lose a velocity

    if ball.position.y <= 0:
        ball.position.y = 0
        ball.vy *= -1

    x = int(ball.position.x)
    y = int(ball.position.y)
    if 0 <= y < sceneY and 0 <= x < sceneX:
        sceneArray[y][x] = '@'
    ball.vx *= 0.99 #deceleration
    printScene()
    time.sleep(1/fps)