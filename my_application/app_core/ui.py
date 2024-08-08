import functions as f
import menus

keep_going = True
while keep_going:
    menus.display_menu()
    user_choice = input("enter choice: ")
    if user_choice == "1":
        user_name = input("enter your name: ")
        print(f.greet_user(user_name))
    elif user_choice == "2":
        a = int(input("enter first number: "))
        b = int(input("enter second number: "))
        sum_ = f.sum_of_numbers(a, b)
        print(f"the sum is {sum_}")
    elif user_choice == "3":
        numbers = []
        n = int(input("enter number: "))
        numbers.append(n)
        while True:
            more_numbers = input("do you want to add more numbers? y/n: ")
            if more_numbers == "y":
                n = int(input("enter number: "))
                numbers.append(n)
            else:
                break
        max_ = f.get_max(numbers)
        print(f"the max value is: {max_}")
    elif user_choice == "4":
        area = f.get_circle_area(float(input("enter radius: ")))
        print(f"area is: {area}")
    elif user_choice == "5":
        celsius = f.get_celsius(float(input("enter degrees in fahrenheit: ")))
        print(f"degrees in celsius are: {celsius}")
    elif user_choice == "find":
        print(f"definition: {f.find_word_in_dictionary(input("enter word: "))}")
    elif user_choice == "add":
        word = input("enter word: ")
        definition = input("enter definition: ")
        f.add_entry_to_dictionary(word, definition)
        print(f"the word {word} added to dictionary")
    elif user_choice == "x":
        keep_going = False
    else:
        print(f"Error: the choice {user_choice} is not supported yet")

print("Bye")
