import math

dictionary = {"python": "a programming language", "dog": "a nice animal"}


# print(dictionary["dog"])

def add_entry_to_dictionary(word: str, definition: str):
    dictionary[word] = definition


def find_word_in_dictionary(word: str) -> str:
    if dictionary.__contains__(word):
        return dictionary[word]
    else:
        return "NOT FOUND"


def get_celsius(fahrenheit: float) -> float:
    celsius = ((fahrenheit - 32) * 5) / 9
    return celsius


def get_circle_area(radius: float) -> float:
    area = math.pi * (radius ** 2)
    return area


def greet_user(user_name: str):
    return f"Hello, {user_name}"


def sum_of_numbers(a: int, b: int) -> int:
    return a + b


def get_max(list_of_numbers: list[int]) -> int:
    max_ = list_of_numbers[0]
    for n in list_of_numbers:
        if n > max_:
            max_ = n
    return max_
