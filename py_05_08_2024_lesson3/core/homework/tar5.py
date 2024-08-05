sum_ = 0
count = 0
n = int(input("enter value: "))

while n != -1:
    sum_ += n
    count += 1
    n = int(input("enter value: "))

if count > 0:
    avg = sum_ / count
    print(f"average is {avg}")
else:
    print("no data")

