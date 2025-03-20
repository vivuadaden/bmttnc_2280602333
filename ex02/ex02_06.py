input_str = input ("nhap X, Y: ")
dimenstion= [int(x) for x in input_str.split(',')]
rowNum = dimenstion[0]
colNum = dimenstion[1]
multilist = [[0 for col in range(colNum)] for row in range (rowNum)]
for row in range (rowNum):
    for col in range (colNum):
        multilist[row][col]=row*col
print(multilist)