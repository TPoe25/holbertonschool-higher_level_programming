# ask for a string
new_string = input("convert to acronym: ")
# convert the string to uppercase
new_string = new_string.upper()
# convert the string into a list
word_list = new_string.split()
# cycle through the list
for word in word_list:
    # Get the 1st letter of the word and eliminate the newline
    print(word[0], end="")
# add a newline
print()
