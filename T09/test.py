number = int(input("How many times should we joe mama this txt file?\n"))

for times in range(number):
    with open("joemama.txt", "a") as file:
        file.write(f"joe mama deez\n")

# making sure i know whats what
print(number)
print(times)
print(file)

user_file = str(input("What would you like to name your copy of equations.txt?\n").strip(".txt"))
with open("joemama.txt") as file:
        lines = file.readlines()
        for line in lines:
            set = line.strip()
            print(set)
        with open(f"{user_file}.txt", "w") as new_file:
             for line in lines:
                new_file.write(f"{set}\n")