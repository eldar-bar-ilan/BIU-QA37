secret_password = "123"
trials = 1

user_input = input("enter password to login: ")

while trials < 3 and user_input != secret_password:
    print("wrong password. try again")
    user_input = input("enter password to login: ")
    trials = trials + 1

if user_input == secret_password:
    print("Good! you are logged in")
else:
    print("login failed")

