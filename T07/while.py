# Start loop
# Ask for number
# if number not == -1, add that number to the_bag, add 1 to counter, continue loop
# if number == -1, the_bag / counter, print, break loop
while True:
    the_bag = 0
    counter = 0
    while True:

        lets_go = int(input("Hello please enter a number, enter -1 to get the average of all the numbers entered (excluding -1\n"))

        if lets_go != -1:
            the_bag += lets_go
            counter += 1
            continue
        elif lets_go == -1:
            the_answer = the_bag / counter
            print(the_answer)
            break
    
    # Asking if user wants to use the tool again
    again = input("Would you like to go again? y/n\n").lower()
    if again == "y":
        continue
    else:
        break