# variable to add * to
stars = ""

# what I want at the end
goal = "*****"

# for loop goes through a range based on the length of the variable 'goal'
# everytime it does, it adds a '*' to the variable 'stars' and prints it
for i in range(len(goal)):
    stars += "*"
    print(stars)
