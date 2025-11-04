import os

#Variables
sceneX = 50
sceneY = 25

sceneArray = [

]

# clear terminal screen def
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# draw blank screen def
def drawBlank():
    clear()
    for i in range(sceneY):
        sceneRow = ['`']*sceneX
        sceneArray.append(sceneRow)
    
drawBlank()

for sublist in sceneArray:
    print(" ".join(map(str, sublist)))

# while True:
#     #Physics 
    
#     #Ascii Rendering
#     clear()
#     break