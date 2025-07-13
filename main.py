import random
import string
import tkinter as tk
from tkinter import messagebox

# Генерація пароля
def generate_password(length, use_specials=True):
    if length < 8 or length > 32:
        raise ValueError("Довжина пароля повинна бути від 8 до 32 символів")

    letters = string.ascii_letters
    digits = string.digits
    punctuation = "!@#$%^&*()-_=+[]{};:,.<>?"

    if use_specials:
        all_chars = letters + digits + punctuation
        base = [
            random.choice(letters),
            random.choice(digits),
            random.choice(punctuation)
        ]
    else:
        all_chars = letters + digits
        base = [
            random.choice(letters),
            random.choice(digits)
        ]

    for _ in range(length - len(base)):
        base.append(random.choice(all_chars))

    random.shuffle(base)
    return ''.join(base)

#Кнопки
def on_generate():
    try:
        length = int(length_entry.get())
        use_specials = special_var.get()
        password = generate_password(length, use_specials)
        result_var.set(password)
    except ValueError as e:
        messagebox.showerror("Помилка", str(e))

def on_copy():
    password = result_var.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Скопійовано", "Пароль скопійовано в буфер обміну!")
    else:
        messagebox.showwarning("Увага", "Спочатку згенеруйте пароль!")

#Темна тема
BG_COLOR = "#1e1e1e"
FG_COLOR = "#dcdcdc"
BTN_COLOR = "#333333"
ENTRY_COLOR = "#2d2d2d"

root = tk.Tk()
root.title("Генератор Паролів")
root.geometry("400x300")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

#Інтерфейс
tk.Label(root, text="Довжина пароля (8-32):", bg=BG_COLOR, fg=FG_COLOR).pack(pady=10)

length_entry = tk.Entry(root, justify='center', bg=ENTRY_COLOR, fg=FG_COLOR, insertbackground=FG_COLOR)
length_entry.pack()
length_entry.insert(0, "14")

# Чекбокс: використовувати спецсимволи чи ні
special_var = tk.BooleanVar(value=True)
special_checkbox = tk.Checkbutton(root, text="Використовувати спецсимволи", variable=special_var,
                                  bg=BG_COLOR, fg=FG_COLOR, selectcolor=BG_COLOR, activebackground=BG_COLOR,
                                  activeforeground=FG_COLOR)
special_checkbox.pack(pady=5)

tk.Button(root, text="Генеруємо"
                     "", command=on_generate, bg=BTN_COLOR, fg=FG_COLOR).pack(pady=10)

result_var = tk.StringVar()
result_entry = tk.Entry(root, textvariable=result_var, font=("Arial", 12), justify='center',
                        state='readonly', bg=ENTRY_COLOR, fg=FG_COLOR, readonlybackground=ENTRY_COLOR)
result_entry.pack(pady=5)

tk.Button(root, text="Скопіювати пароль", command=on_copy, bg=BTN_COLOR, fg=FG_COLOR).pack(pady=10)

tk.Label(root, text="Створив lilsento", bg=BG_COLOR, fg="#777777").pack(side="bottom", pady=5)

root.mainloop()
