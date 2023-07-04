import copy
# defining the minefield
minefield  = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"] ]

# creating a copy of the minefield to modify
new_minefield  = copy.deepcopy(minefield)

# defining a function that replaces "-" with a 0
def ribosome():
    rows = len(minefield)                       # makes sure of the number of rows in minefield = 5
    for row in range(rows):                     # for each row in however many rows...
        cols = len(minefield[row])              # cols will be the length of the current row
        for col in range(cols):                 # for each column in however many columns...
            if minefield[col][row] == "-":      # if that position is "-"...
                new_minefield[col][row] = 0     # turn that position into a 0

# defining functions that check around a position
# if the current position isn't "#" AND the direction doesn't go out of bounds AND...
# ...if an adjecent postion is "#" it adds 1 to the position in the new_minefield only 
def NW():
    rows = len(minefield)
    for row in range(rows):
        cols = len(minefield[row])
        for col in range(cols):
            if col > 0 and row > 0 and minefield[col-1][row-1] == "#" and minefield[col][row] != "#":
                new_minefield[col][row] += 1
def N():
    rows = len(minefield)
    for row in range(rows):
        cols = len(minefield[row])
        for col in range(cols):
            if row > 0 and minefield[col][row-1] == "#" and minefield[col][row] != "#":
                new_minefield[col][row] += 1
def NE():
    rows = len(minefield)
    for row in range(rows):
        cols = len(minefield[row])
        for col in range(cols):
            if col < cols -1 and row < rows - 1 and minefield[col+1][row-1] == "#" and minefield[col][row] != "#":
                new_minefield[col][row] += 1
def W():
    rows = len(minefield)
    for row in range(rows):
        cols = len(minefield[row])
        for col in range(cols):
            if col > 0 and minefield[col-1][row] == "#" and minefield[col][row] != "#":
                new_minefield[col][row] += 1
def E():
    rows = len(minefield)
    for row in range(rows):
        cols = len(minefield[row])
        for col in range(cols):
            if col < cols - 1 and minefield[col+1][row] == "#" and minefield[col][row] != "#":
                new_minefield[col][row] += 1
def SW():
    rows = len(minefield)
    for row in range(rows):
        cols = len(minefield[row])
        for col in range(cols):
            if col > 0 and row < rows - 1 and minefield[col-1][row+1] == "#" and minefield[col][row] != "#":
                new_minefield[col][row] += 1
def S():
    rows = len(minefield)
    for row in range(rows):
        cols = len(minefield[row])
        for col in range(cols):
            if row < rows - 1 and minefield[col][row+1] == "#" and minefield[col][row] != "#":
                new_minefield[col][row] += 1
def SE():
    rows = len(minefield)
    for row in range(rows):
        cols = len(minefield[row])
        for col in range(cols):
            if col < cols - 1 and row < rows - 1 and minefield[col+1][row+1] == "#" and minefield[col][row] != "#":
                new_minefield[col][row] += 1


ribosome()
NW()
N()
NE()
W()
E()
SW()
S()
SE()
print(new_minefield)


[[1, 1, 2, '#', '#'], 
 [1, '#', 3, 3, 2], 
 [2, 4, '#', 2, 0], 
 [1, '#', '#', 2, 0], 
 [1, 2, 2, 1, 0]]
