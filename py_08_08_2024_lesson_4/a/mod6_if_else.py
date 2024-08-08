grade = int(input("enter grade: "))
print(f"the grade entered is {grade}")

if 0 <= grade < 55:
    print("fail")
elif 55 <= grade < 70:
    print("pass")
elif 70 <= grade < 80:
    print("good")
elif 80 <= grade <= 100:
    print("excellent")
else:
    print(f"INPUT ERROR: the value {grade} is out of range")




