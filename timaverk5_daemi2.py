n = int(input("Enter the length of the sequence: ")) # Do not change this line

# forrit sem gefur út fyrstu n tölurnar í runu
# runan: 1, 2, 3, 6, 11, 20, 37...

for i in range(1,n+1):
    if i == 1:
        tala1  = 1
        print(tala1)
    elif i == 2:
        tala2 = 2
        print(tala2)
    elif i == 3:
        tala3 = 3
        print(tala3)
    else:
        summa = tala1+tala2+tala3
        tala1 = tala2
        tala2 = tala3
        tala3 = summa
        print(summa)

