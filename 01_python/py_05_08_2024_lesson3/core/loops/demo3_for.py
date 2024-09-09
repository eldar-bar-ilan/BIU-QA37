numbers = []
c = 1
is_even = False

while c <= 5:
    x = int(input("enter number: "))
    if x % 2 == 0:
        is_even = True
    numbers.append(x)
    c += 1

print(numbers)
print(f"contains even numbers? {is_even}")
