import math
while True:
# Using while loop to validate investment or bond input from user
# input().lower() will not make user answer case-sensitive
    print("investment - to calculate the amount of interest you'll earn on your investment \nbond       - to calculate the amount you'll have to pay on a home loan")
    while True:
        user_choice = input(
            "Enter either 'investment' or 'bond' from the menu above to proceed:\n").lower()
        if user_choice == "investment":
            break
        elif user_choice == "bond":
            break
        else:
            print("Sorry, please enter either investment or bond to proceed")
            continue
# investment will ask for user input of 1. Money_amount 2. Interest_amount 3. Years number
# will validate interest_amount to int(input().strip("%")) to remove any "%" from input and make it an integer
# 4. Ask for simple or compound interest
# Excecute math and display.
    while True:
        if user_choice == "investment":
            money = int(input("How much money are you depositing?\n"))
            interest_amount = int(input("What is the interest rate?\n").strip("%")) / 100
            years_number = int(input("How many years are you investing for?\n"))
            interest = input("Would you like simple or compound interest?\n").lower()
#while loop to enable user to switch to compound or simple interest after seeing their results
            while True: 
                if interest == "simple":
                    simple_interest = money * (1 + interest_amount*years_number)
                    print(f"SIMPLE INTEREST: Your investment of £{money} at an interest of {int(interest_amount*100)}% over {years_number} years will be £{simple_interest} at the end")
                    simple_to_compound = input("Would you like to see compound interest? y/n\n").lower()
                    if simple_to_compound == "y":
                        interest = "compound"
                        continue
                    else:
                        break
                elif interest == "compound":
                    compound_interest = money * math.pow((1+interest_amount), years_number)
                    print(f"COMPOUND INTEREST: Your investment of £{int(money)} at an interest of {int(interest_amount*100)}% over {years_number} years will be £{compound_interest} at the end")
                    compound_to_simple = input("Would you like to see simple interest? y/n\n").lower()
                    if compound_to_simple == "y":
                        interest = "simple"
                        continue
                    else:
                        break
                break
            break
# if user chooses bond, ask for 1. house price 2. interest_amount / 100 3. number of months
# excecute maths
        elif user_choice == "bond":
            house = int(input("What's the current price of the house?\n"))
            annual_interest_rate = float(input("What's the interest rate?\n").strip("%")) / 100
            monthly_interest_rate = annual_interest_rate / 12
            months = int(input("Over how many months do you plan on repaying the bond?\n"))
            repayment = (monthly_interest_rate * house) / (1 - math.pow(1 + monthly_interest_rate, -months))
            print(f"You will have to repay £{repayment:.2f} per month based on a £{house} house at an interest rate of {annual_interest_rate*100}% over {months} months")
            break
        else:
            print("Sorry please enter either simple or compound to continue")
            continue
# while loop to ask if the user wants to use the tool from the beginning
    question = input("Would you like to use this tool from the beginning? y/n\n").lower()
    if question == "y":
        continue
    elif question == "n":
        print("Thanks for using the tool!")
        break