import math

while True:
    # Print menu and get user choice
    print("INVESTMENT - to calculate the amount of interest you'll earn on your investment \nBOND       - to calculate the amount you'll have to pay on a home loan")
    for i in range(3):  # Try up to 3 times to get valid input
        investment_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed:\n").lower()
        if investment_choice in ["investment", "bond"]:
            break  # Valid input received, exit loop
        else:
            print("Sorry, please enter either 'investment' or 'bond' to proceed")

    # Calculate investment or bond based on user choice
    if investment_choice == "investment":
        for i in range(3):  # Try up to 3 times to get valid input
            try:
                money = int(input("How much money are you depositing?\n"))
                interest_rate = int(input("What is the interest rate?\n").strip("%")) / 100
                years = int(input("How many years are you investing for?\n"))
                interest_type = input("Would you like simple or compound interest?\n").lower()
                if interest_type in ["simple", "compound"]:
                    break  # Valid input received, exit loop
                else:
                    print("Sorry, please enter either 'simple' or 'compound' to proceed")
            except ValueError:
                print("Sorry, please enter a valid integer")

        if interest_type == "simple":
            simple_interest = money * (1 + interest_rate * years)
            print(f"SIMPLE INTEREST: Your investment of £{money} at an interest of {int(interest_rate*100)}% over {years} years will be £{simple_interest} at the end")
        else:
            compound_interest = money * math.pow((1+interest_rate), years)
            print(f"COMPOUND INTEREST: Your investment of £{int(money)} at an interest of {int(interest_rate*100)}% over {years} years will be £{compound_interest} at the end")

    else:  # investment_choice == "bond"
        for i in range(3):  # Try up to 3 times to get valid input
            try:
                house_price = int(input("What's the current price of the house?\n"))
                interest_rate = int(input("What's the interest rate?\n").strip("%")) / 100
                months = int(input("Over how many months do you plan on repaying the bond?\n"))
                break  # Valid input received, exit loop
            except ValueError:
                print("Sorry, please enter a valid integer")

        repayment = (interest_rate * house_price) / (1 - (1 + interest_rate) ** (-months))
        print(f"You will have to repay £{repayment:.2f} per month based on a £{house_price} house at an interest rate of {interest_rate*100:.2f}%")
