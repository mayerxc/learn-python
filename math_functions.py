#Determine hypotenuse of a triangle with sides 15 and 17
import math
import random

print('Hypotenuse of triangle with sides 15 and 17:')
answer = math.hypot(15, 17)
print(answer, "\n")


print("180 degress is:", math.radians(180), "radians." )
print("2 radians is:", math.degrees(2), "degrees.")
print("270 degrees is:", math.radians(270), "radians.")
print('5 radians is', math.degrees(5), "degrees.", "\n")

x = 0
sum = 0
while ( x < 100 ):
    number = random.randrange(1, 10)
    print(number)
    sum =  number + sum
    x += 1
print("Sum of all random numbers:", sum)
print("Average of random numbers:", sum / x)