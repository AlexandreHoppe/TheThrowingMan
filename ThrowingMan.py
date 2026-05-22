import time

rows, cols = (50, 100)
visualList = [[" " for i in range(cols)] for j in range(rows)]
visualList[-1] = ["_"]*cols * 1

visualList[-3][0] = "/"
visualList[-1][0]= "/"

visualList[-3][1] = "\\"
visualList[-1][1]= "\\"

visualList[-2][0]= " |"
visualList[-2][1]= "*"
visualList[-4][0]= " 0"

for w in range(len(visualList)) :
    print(*visualList[w], end="\n")


throwForce = int(input("Enter the Throwing strenght : "))

for x in range(throwForce * 2) :
    if x > throwForce :
        
    yPos = x**2 + 2
    visualList[-x - 2][yPos-1]= "*" 
    time.sleep(1)

    for w in range(len(visualList)) :
        print(*visualList[w], end="\n")