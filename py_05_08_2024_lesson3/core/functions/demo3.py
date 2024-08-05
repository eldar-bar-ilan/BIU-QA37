def print_name():
    print("Eldar")
    print("Eldar")
    print("Eldar")


def greet(user_name: str):
    print(f"Hello {user_name}")


def send_greet(user_name) -> str:
    return f"Hello {user_name}"


# print_name()
greet("Dan")
greet_message = send_greet("Lea")
print(greet_message)
