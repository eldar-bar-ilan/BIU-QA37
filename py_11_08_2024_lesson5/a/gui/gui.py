import tkinter as tk

# create the main window
root = tk.Tk()
# set default font
root.option_add("*Font", ("Arial", 12, "normal"))
# size and location
root.geometry("500x300")
root.title("Eldar's App")

# to display text we use label objets
lb_name = tk.Label(root, text="enter name", borderwidth=1, relief="solid", width=10, anchor="w")
lb_name.place(x=20, y=20)
tf_name = tk.Entry(root, width=30)
tf_name.place(x=130, y=20)

lb_age = tk.Label(root, text="enter age", borderwidth=1, relief="solid", width=10, anchor="w")
lb_age.place(x=20, y=50)
tf_age = tk.Entry(root, width=5)
tf_age.place(x=130, y=50)

bt_msg = tk.Button(text="Click")
bt_msg.place(x=20, y=80)


# callback function
def greet():
    user_name = tf_name.get()
    print(user_name)


# register the button with the function
bt_msg.config(command=greet)

# display - the last line
root.mainloop()
print("Bye")
