import random

grade = random.randint(0, 100)
print("grade is", grade)

if grade >= 90:
    print("Excellent")
elif grade >= 80:
    print("Good")
elif grade >= 70:
    print("Average")
else:
    print("You need to improve")
