# Physics Varables
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