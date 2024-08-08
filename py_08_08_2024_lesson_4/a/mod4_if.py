import random

age = random.randint(0, 80)
print(f"the age is {age}")

if age >= 18:
    print("you are an adult")
    print("you can have a driving license")
if 60 <= age <= 80:
    print("you are senior")
    print("you can have discount on transportation")
print("end of program")



