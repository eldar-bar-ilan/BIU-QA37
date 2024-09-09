x = int(input("enter a number: "))
print(x)
y = 0

while x != 0:
    y *= 10
    y += x % 10
    x //= 10

print(y)
