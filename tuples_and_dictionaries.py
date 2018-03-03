gpas = (3.14, 3.45, 3.98, 2.55, 3.24, 2.27)
names = ("Bob", "Mark", "Melissa", "Travis", "DeeDee", "Ian")

print(gpas[1])

sum = 0
dictionary = {}
for gpa in gpas:
    sum = gpa + sum
    
counter = 0
while counter < len(names):
    dictionary[names[counter]] = gpas[counter]
    counter += 1

print("Average GPA is:", sum / len(gpas))   
print("Dictionary is:", dictionary)
max = max(dictionary, key=dictionary.get )
print(max, "has highest GPA with", dictionary[max],)

min = min(dictionary, key=dictionary.get)
print(min, "has lowest GPA with", dictionary[min],)