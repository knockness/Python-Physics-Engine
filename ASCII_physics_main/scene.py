import os
import subprocess

# Scene Variables
sceneX = 50
sceneY = 67

class Cartesian:
    # Making the array
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.matrix = []
        for i in range(height+1):
                 if i == height:
                     sceneRow = ['']*width #row researved for deubug variables
                     self.matrix.append(sceneRow)
                 elif i == height - 1:
                     sceneRow = ['¯']*width
                     self.matrix.append(sceneRow)
                 else:
                     sceneRow = ['`']*width
                     self.matrix.append(sceneRow)
    # Handles setting items in the array
    def __setitem__(self, coords, value):
        x, y = coords
        self.matrix[(self.height - 1) - y][x] = value
    # Handles getting values in the array
    def __getitem__(self, coords):
        x, y = coords
        return self.matrix[(self.height - 1) - y][x]
    
# Scene Writing
    # clear terminal screen def
def clear():
    subprocess.run(['cls' if os.name == 'nt' else 'clear'], shell=True)

    # Print Written Scene def
def printScene():
    clear()
    for sublist in sceneArray.matrix:
        print(" ".join(map(str, sublist)))

    # draw blank screen def
def drawBlank():
    clear()
    global sceneArray
    sceneArray = Cartesian(sceneX, sceneY)