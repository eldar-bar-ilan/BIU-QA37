numbers = [22, 456, 12, -9, 45]
sum_ = 0
min_ = numbers[0]
max_ = numbers[0]

for x in numbers:
    sum_ += x
    if x > max_:
        max_ = x
    if x < min_:
        min_ = x

avg = sum_ / len(numbers)
print(f"sum: {sum_}, average: {avg}, minimum: {min_}, maximum: {max_}")

