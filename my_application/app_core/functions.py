def greet_user(user_name: str):
    return f"Hello, {user_name}"


def sum_of_numbers(a: int, b: int) -> int:
    return a + b


def get_max(list_of_numbers) -> int:
    sum_ = 0
    for n in list_of_numbers:
        sum_ += n
    return sum_
