num_int = int(input("Input a number: ")) # Do not change this line
# Fill in the missing code
max_int = 0 #núllstilla samanburðartöluna
while num_int >= 0:
    if num_int > max_int: #ef num_int er stærra en stærsta talan sem komin er
        max_int = num_int #þá verður num_int nýja max_int
    num_int = int(input("Input a number: "))

print("The maximum is", max_int) # Do not change this line
