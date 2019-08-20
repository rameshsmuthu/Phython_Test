import random

number = random.randint(1,10)

guess = 0

while True:
    num_input = input("please input one integer that is in 1 to 10:")
    guess += 1

    if not num_input.isdigit():
        print("Please input interger.")
    elif int(num_input) < 0 or int(num_input) >= 10:
        print("The number should be in 1 to 10.")
    else:
        if number == int(num_input):
            print("OK, you are good. you tried %d times, then you successed." % guess)
            break
        elif number > int(num_input):
            print("your number is smaller.")
        elif number < int(num_input):
            print("your number is bigger.")
        else:
            print("There is something bad, I will not work")