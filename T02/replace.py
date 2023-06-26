single_string = "The!quick!brown!fox!jumps!over!the!lazy!dog!."
print(single_string)
# using replace() to replace "!" with " "
no_exclamations = single_string.replace("!"," ")
print(no_exclamations)
# using upper() to make it uppercase
uppercase = no_exclamations.upper()
print(uppercase)
# reversing the string uhh
reverse = uppercase[::-1]
print(reverse)
# uppercase[0] gets the first character
# uppercase[-1] gets the last
# uppercase[6:12] gets a slice from position 6 to 12 not including 12
# uppercase[4:] gets a slice from 4 to the end
# uppercase[:8] gets a slice from the start to 8 not including 8
# uppercase[:] gets a slice from the start to the end
# uppercase[::-1] is [where you want to start: where you want to end:step] that will print from the last character to the start
# step is a modifier so [::-1] prints it backwards [::1] prints it forwards [::2] does this:
print(uppercase[::2])
# prints every 2nd character