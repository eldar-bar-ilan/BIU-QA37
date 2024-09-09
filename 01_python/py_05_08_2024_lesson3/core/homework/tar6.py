n = int(input("enter value: "))
max_ = n
c = 0

while n != -1:
    c += 1
    if n > max_:
        max_ = n
    n = int(input("enter value: "))

if c > 0:
    print(f"maximum is: {max_}")
else:
    print("no data")

