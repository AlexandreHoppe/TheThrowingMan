rows, cols = (10, 20)
visualList = [[" " for i in range(cols)] for j in range(rows)]
visualList[-1] = ["_"]*cols * 1

visualList[-3][1] = "/"
visualList[-1][1]= "/"

visualList[-3][2] = "\\"
visualList[-1][2]= "\\"

visualList[-2][1]= " |"

visualList[-4][1]= " O"

for w in range(len(visualList)) :
    print(*visualList[w], end="\n")
