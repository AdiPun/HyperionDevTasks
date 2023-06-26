# casting input into string
# creating an empty list to add characters to
# for loop with l.append(each character)
# elif %2 to if if the charcter index is even/odd
# " ".join() to join the item in the list into a single string

string = str(input("Enter your string\n"))

string_list = []

for count, character in enumerate(string):
    if count % 2 == 0:
#        print(count, character) debugging
        string_list.append(character.upper())
    elif count % 2 != 0:
#        print(count, character) debugging
        string_list.append(character.lower())

string_alternative = " ".join(string_list)

print(string_alternative)

# printing each other word as upper or lower case
# splitting string into a list
# .upper and .lower depending on the position being even/odd

split_string = string.split(" ")
word_list = []

for count, word in enumerate(split_string):
    if count % 2 == 0:
        word_list.append(split_string[count].upper())
    elif count % 2 != 0:
        word_list.append(split_string[count].lower())

word_alternative = " ".join(word_list)

print(word_alternative)