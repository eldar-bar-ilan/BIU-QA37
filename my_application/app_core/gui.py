import tkinter as tk
import functions as f

root = tk.Tk()
root.title("Dictionary")
root.geometry("685x340")

fr1 = tk.Frame(root, borderwidth=1, relief="solid", background="#5f9596")
lb_dictionary_words = tk.Label(fr1, text='Dictionary Words', width=20)
bt_remove_word = tk.Button(fr1, text='remove word', width=10)
bt_add_or_edit_word = tk.Button(fr1, text='add/edit word', width=10)
text_variable = tk.StringVar()
# text_variable.set("")
ent_word = tk.Entry(fr1, width=20, borderwidth=1, relief="solid", font=("", 14), textvariable=text_variable)
bt_find_word = tk.Button(fr1, text='find words', width=10)
word_list = tk.Listbox(fr1, width=22, height=15)
txt_def = tk.Text(fr1, width=60, height=15)

lb_dictionary_words.grid(row=0, column=0, padx=10, pady=10, columnspan=1)
bt_add_or_edit_word.grid(row=0, column=1, sticky='w', columnspan=1)
bt_find_word.grid(row=0, column=2, sticky='e', columnspan=1)
bt_remove_word.grid(row=0, column=4, sticky='w', columnspan=1)
ent_word.grid(row=0, column=3, columnspan=1)

word_list.grid(row=1, column=0, sticky="n", pady=10, rowspan=2, columnspan=1)
txt_def.grid(row=1, column=1, rowspan=2, columnspan=4, pady=10)

fr1.pack(side='top', fill="x", padx=10, pady=10)


def show_words():
    words = f.dictionary.keys()
    word_list.delete(0, tk.END)
    for w in words:
        word_list.insert(tk.END, w)


def add_word():
    word = ent_word.get()
    if word:
        definition = txt_def.get('1.0', tk.END)
        f.add_entry_to_dictionary(word, definition)
        show_words()


def remove_word():
    word = ent_word.get()
    if word:
        f.remove_from_dictionary(word)
        show_words()


def find_word():
    word = ent_word.get()
    if word:
        definition = f.find_word_in_dictionary(word)
        txt_def.delete('1.0', tk.END)
        txt_def.insert('1.0', definition)


def on_select(event):
    widget = event.widget
    if len(widget.curselection()) == 0:
        return
    index = int(widget.curselection()[0])
    word = widget.get(index)
    text_variable.set(word)
    find_word()


# lb_dictionary_words.config(command=show_words)
bt_add_or_edit_word.config(command=add_word)
bt_remove_word.config(command=remove_word)
bt_find_word.config(command=find_word)
word_list.bind("<<ListboxSelect>>", on_select)

show_words()
tk.mainloop()
