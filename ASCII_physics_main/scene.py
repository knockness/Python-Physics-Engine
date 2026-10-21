import os
import subprocess

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
        self.matrix[(self.height - 1) - y][x] = value # Conversion of y coordinates from 0 being the top to 0 being the bottom to mimic an actual cartesian plane
    # Handles getting values in the array
    def __getitem__(self, coords):
        x, y = coords
        return self.matrix[(self.height - 1) - y][x] # Same conversion
    
# Scene Writing
    # clear terminal screen def
def clear():
    subprocess.run(['cls' if os.name == 'nt' else 'clear'], shell=True)

    # Prints the Scene currently written in the buffer
def printScene(sceneName):
    clear()
    for sublist in sceneName.matrix:
        print(" ".join(map(str, sublist)))

    # defines a scene
def createScene(width, height):
    clear() # Ensures only one scene at a time
    return Cartesian(width, height)