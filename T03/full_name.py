# using elif to validate the correct name length
# using while to ask them again and again until we get what we want
# using continue to skip the code underneath it to minimise wasted processing
# using break to stop the while loop once we've got what we want

full_name = input("Hey user! What's your name?\n")
length = len(full_name)

while True:
    if length == 0:
        full_name = input("You haven't entered anything. Please enter your full name\n")
        length = len(full_name)
        continue
    elif length < 4:
        full_name = input("You've entered less than 4 characters. Please make sure you enter your first and last name\n")
        length = len(full_name)
        continue
    elif length > 25:
        full_name = input("""You've entered more than 25 characters. Please make sure you've only entered your first and last name\n""")
        length = len(full_name)
        continue
    else:
        print(f"Thank you, {full_name} for entering your name!")
    break