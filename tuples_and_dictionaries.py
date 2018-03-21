gpas = (3.14, 3.45, 3.98, 2.55, 3.24, 2.27)
names = ("Bob", "Mark", "Melissa", "Travis", "DeeDee", "Ian")

print(gpas[1])

sum = 0
dictionary = {}
dictionary2 = {}
for gpa in gpas:
    sum = gpa + sum

# while loop of creating dictionary
counter = 0
while counter < len(names):
    dictionary[names[counter]] = gpas[counter]
    counter += 1
lNames = list(names)
lGpas = list(gpas)

# for loop way
for name, gpa in zip(names, gpas):
    dictionary2[name] = gpa

print("for loop dictionary2 is:", dictionary2)

print("Average GPA is:", sum / len(gpas))   
print("Dictionary is:", dictionary)

# one way to get max key or min key
max = max(dictionary, key=dictionary.get )
print(max, "has highest GPA with", dictionary[max],)
min = min(dictionary, key=dictionary.get)
print(min, "has lowest GPA with", dictionary[min],)

# another way is to use items
list1 = list()
for key, val in dictionary2.items():
    # create val first list of tuples from dict
    list1.append( (val, key) )
list1.sort(reverse=True)
print(list1[0][1], "has highest GPA with", list1[0][0])
list1.sort()
print(list1[0][1], "has lowest GPA with", list1[0][0])
