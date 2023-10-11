# Ask for their name
name = input("Hello, what is your name? ")

#Ask for their age, make sure it is of type int
age = int(input(f"Hello {name}, what is your age? "))
if age == 0:
    print("That is not a valid age. ")
if age == 16:
    print("Congratulations, you can drive! ")
if age == 17:
    print("You're almost eligible to vote. At least you can drive! ")
if age >= 18 and age < 21:
    print("You're eligible to vote. ")
if age >= 21 and age < 55:
    print("You can enjoy a beer")
if age >= 55:
    print("You get the senior discount")
if age >= 100:
    print("Wow, you are old!")