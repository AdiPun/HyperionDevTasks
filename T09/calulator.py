# assigning the first two numbers and the operator
# using try except blocks to validate inputs
# using elif blocks to validate operator input

while True:

    while True:
        try:
            first_number = float(input("Please enter your first number\n"))
            break
        except ValueError:
            print("Whoops! Please enter a valid number...")
    while True:
        try:
            second_number = float(input("Please enter your second number\n"))
            break
        except ValueError:
            print("Whoops! Please enter a valid number...")
    # using all inputed variables to output the equation using elif
    while True:
        operation = str(
            input("Please enter the operator you'd like to perform on the two numbers\n"))
        if operation == "+":
            equation = (
                f"{first_number} {operation} {second_number} = {first_number + second_number}")
            break
        elif operation == "-":
            equation = (
                f"{first_number} {operation} {second_number} = {first_number - second_number}")
            break
        elif operation == "*":
            equation = (
                f"{first_number} {operation} {second_number} = {first_number * second_number}")
            break
        elif operation == "/":
            equation = (
                f"{first_number} {operation} {second_number} = {first_number / second_number}")
            break
        else:
            print("Whoops! Please enter either + - * /")
            continue
    # appending the equation to a txt file
    print("Your equation was:")
    print(equation)
    with open("equations.txt", "a") as file:
        file.write(f"{equation}\n")
    # elif loop to ask the user if they want to do another calculation
    # or view the past equations by opening the text file
    # try except finally to give info if equations.txt file not found
    # with  open() as  to open equations.txt to create a set from file.readlines()
    # for loop to .write() the set into user created txt file

    while True:
        again = input(
        "Type A if you would like to do do a calculation again\nType B if you'd like to read all the past equations from a txt file\n").upper()
        if again == "A":
            again = True
            break
        elif again == "B":
            again = False
            break
        else:
            print("Sorry please type A or B")
            continue
    
    # trying to make the loop work from the beginning

    if again == True:
        continue
    elif again == False:
        break

user_file = str(
        input("What would you like to name your copy of equations.txt?\n").strip(".txt"))

try:
    with open("equations.txt", "r") as file:
        lines = file.readlines()
#        print(lines)  debugging
        for line in lines:
            print(line)
        with open(f"{user_file}.txt", "w") as user_file:
            for line in lines:
                user_file.write(f"{line}")
except FileNotFoundError as error:
    print("File 'equations.txt not found!")
    print(error)