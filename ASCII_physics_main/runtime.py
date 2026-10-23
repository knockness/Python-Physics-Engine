# Default Python Imports
import time

# Project Imports
import globals
import objects
import scene

# Rendering variables
fps = 60

# pixels per meter
ppm = 7

prevPositon = []

myScene = scene.createScene(50, 67)

prevTime = time.perf_counter()
    
# Runtime Loop
while True:
    # Calculate delta time
    currentTime = time.perf_counter()
    globals.deltaTime = currentTime - prevTime
    prevTime = currentTime
    # Physics 


    # Ascii Rendering
    scene.printScene(myScene)
    time.sleep(1/fps)