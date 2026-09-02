import os

# Scene Variables
sceneX = 50
sceneY = 67
sceneArray = [

]

# Scene Writing
    # clear terminal screen def
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    # Print Written Scene def
def printScene():
    clear()
    for sublist in sceneArray:
        print(" ".join(map(str, sublist)))
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