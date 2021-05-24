import random
print("This is a dice stimulator")
x="y"

while x=="y":
        number = random.randint(1, 6)

        if number == 1:
                print("___________")
                print("|         |")
                print("|    o    |")
                print("|         |")
                print("-----------")

        if number == 2:
                print("___________")
                print("|         |")
                print("|  o   o  |")
                print("|         |")
                print("-----------")

        if number == 3:
                print("___________")
                print("|         |")
                print("| o  o  o |")
                print("|         |")
                print("-----------")

        if number == 4:
                print("___________")
                print("|  o    o  |")
                print("|          |")
                print("|  o    o  |")
                print("-----------")

        if number == 5:
                print("___________")
                print("|   o   o  |")
                print("|     o    |")
                print("|   o   o  |")
                print("-----------")

        if number == 6:
                print("___________")
                print("|   o   o  |")
                print("|   o   o  |")
                print("|   o   o  |")
                print("-----------")
        x=input("press y to roll again")


       


