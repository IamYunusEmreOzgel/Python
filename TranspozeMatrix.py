Rows = int(input("How many rows would you like to have? : " ))
Columns = int(input("How many Columns would you like to have?: "))



Matrix= [[int(input()) for i in range(Columns)] for i in range(Rows)]

print("Start entering the elements:")

print("The Matrix Given By User")
for a in Matrix:
    print(a)

transpozeMatrix =[[0 for i in range(Rows)] for j in range(Columns)]

for r in range(Rows):   
   for c in range(Columns):
       transpozeMatrix[c][r] = Matrix[r][c]

print("Transpose Of The Matrix: ")
for b in transpozeMatrix:
    print(b)