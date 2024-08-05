import functions as f
import menus

keep_going = True
while keep_going:
    menus.display_menu()
    user_choice = input("enter choice: ")
    if user_choice == "1":
        user_name = input("enter your name: ")
        print(f.greet_user(user_name))
    if user_choice == "2":
        a = int(input("enter first number: "))
        b = int(input("enter second number: "))
        sum_ = f.sum_of_numbers(a, b)
        print(f"the sum is {sum_}")
    if user_choice == "x":
        keep_going = False

print("Bye")
