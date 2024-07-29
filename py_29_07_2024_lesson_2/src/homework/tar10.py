number = float(input("enter a number: "))
next_number = int(number) + 1
next_number = next_number + (next_number % 2)
print(next_number)
