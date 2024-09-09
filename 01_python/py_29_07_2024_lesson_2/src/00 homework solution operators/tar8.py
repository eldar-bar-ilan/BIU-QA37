x = int(input("enter a 2 digit number: "))
right_digit = x % 10
left_digit = x // 10

y = right_digit * 10 + left_digit
print(y)
