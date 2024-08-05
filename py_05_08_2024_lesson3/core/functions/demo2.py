def print_name():
    print("Eldar")
    print("Eldar")
    print("Eldar")


def greet(user_name):
    print(f"Hello {user_name}")


def send_greet(user_name):
    return f"Hello {user_name}"


# print_name()
# greet("Dan")
greet_message = send_greet("Lea")
print(greet_message)
