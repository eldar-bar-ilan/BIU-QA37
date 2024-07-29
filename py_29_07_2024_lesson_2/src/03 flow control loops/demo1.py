secret_password = "123"

user_input = input("enter password to login: ")

while user_input != secret_password:
    print("wrong password. try again")
    user_input = input("enter password to login: ")

print("Good! you are logged in")
