subjectList = ["English", "Spanish", "Algebra", "Geography", "Theater"]
gpas = [3.12, 3.45, 2.99]

if subjectList[0] == "Geography":
    takingGeography = True
elif subjectList[1] == "Geography":
    takingGeography = True
elif subjectList[2] == "Geography":
    takingGeography = True
elif subjectList[3] == "Geography":
    takingGeography = True
elif subjectList[4] == "Geography":
    takingGeography = True
else:
    takingGeography == False

print("taking geography?", takingGeography)

average = (gpas[0] + gpas[1] + gpas[2]) / len(gpas)
print("average is:", round( (average), 2 ))