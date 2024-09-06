UInput = int(input("Give me a random number! "))
EOO = UInput % 2
MO4 = UInput % 4
if EOO == 0:
    print("You have given me an even number!")
else:
    print("You have given me an odd number!")
if MO4 == 0:
    print("Your number is a multiple of 4!")
else:
    print("Your number is not a multiple of 4!")

num = int(input("Give me a number! "))
check = int(input("Give me a second number!"))
if num % check == 0:
    print("your number evenly divides!")
else:
    print("Your number does not evenly divide :(")
