def takeTranspose(Rows,Columns):
    global transpozeMatrix
    for a in range(Rows):   
        for b in range(Columns):
            transpozeMatrix[b][a] = Matrix[a][b]
        
def printMatrix(matrix):
    for a in matrix:
        print(a)


Rows = int(input("How many rows would you like to have? : " ))
Columns = int(input("How many Columns would you like to have?: "))

Matrix= [[int(input()) for i in range(Columns)] for i in range(Rows)]
transpozeMatrix =[[0 for i in range(Rows)] for j in range(Columns)]

print("Start entering the matrixs elements:")



print("The Matrix Given By User")
printMatrix(Matrix)

takeTranspose(Rows, Columns)

print("Transpose Of The Matrix: ")
printMatrix(transpozeMatrix)
