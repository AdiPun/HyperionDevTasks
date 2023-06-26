# defining the minefield
minefield = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

# creating a new list with the same dimensions as minefield
new_minefield = [[0] * len(minefield[0]) for _ in range(len(minefield))]

# defining a function to check all eight directions
def check_directions(x, y):
    if minefield[x][y] != "#":
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if 0 <= x+dx < len(minefield) and 0 <= y+dy < len(minefield[0]) and minefield[x+dx][y+dy] == "#":
                    new_minefield[x][y] += 1

# using a list comprehension to create a new list where "-" is replaced with 0
minefield = [[0 if c == "-" else c for c in row] for row in minefield]

# looping over each position in the minefield and checking all eight directions
for x in range(len(minefield)):
    for y in range(len(minefield[0])):
        check_directions(x, y)

for x in range(len(minefield)):
    for y in range(len(minefield[0])):
        if new_minefield[x][y] == 0:
            new_minefield[x][y] = "#"

print(new_minefield)
