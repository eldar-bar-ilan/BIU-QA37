# WHILE LOOP

secret_password = "123"

trials = 1
user_input = input("enter password to login: ")

while trials < 3 and user_input != secret_password:
    trials = trials + 1
    print("wrong password. try again (attempt", trials, "of 3)")
    user_input = input("enter password to login: ")

if user_input == secret_password:
    print("Good! you are logged in")
else:
    print("login failed")

print("number of trials:", trials)
