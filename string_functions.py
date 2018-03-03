poem ="With rue my heart is laden\n"
poem +="For golden friends I had\n"
poem +="For many a rose-lipped maiden\n"
poem +="And many a light foot lad\n"
poem +="By brooks too broad for leaping\n"
poem +="The light oot boys are laid\n"
poem +="The rose lipped girls are sleeping\n"
poem +="In fields where roses fade\n"
print(poem)

line = 1
char = 0

while char < len(poem):
    if poem[char] is not "\n":
        if(poem[char].isupper()):
            print("Line #", line, "\t", "Character:", poem[char], "Capital" )
        else:
            print("Line #", line, "\t", "Character:", poem[char], )
    else:
        line += 1

    char += 1


# for letter in poem:
#     if letter is not "\n":
#         if(letter.isupper()):
#             print("Line #", line, "\t", "Character:", letter, "Capital" )
#         else:
#             print("Line #", line, "\t", "Character:", letter, )
#     else:
#         line += 1
#     char += 1