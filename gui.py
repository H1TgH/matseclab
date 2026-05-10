import tkinter as tk
from tkinter import ttk, messagebox

from cipher.text_utils import normalize_text
from cipher.caesar import encrypt, decrypt
from cipher.cracker import crack


def run():
    text = text_input.get("1.0", tk.END).strip()

    if not text:
        messagebox.showerror("Ошибка", "Введите текст")
        return

    text = normalize_text(text)

    mode = mode_var.get()

    try:
        if mode == "encrypt":
            key = int(key_entry.get())
            result = encrypt(text, key)
            output.set(result)

        elif mode == "decrypt":
            key = int(key_entry.get())
            result = decrypt(text, key)
            output.set(result)

        elif mode == "crack":
            key, result = crack(text)
            output.set(f"KEY: {key}\n\n{result}")

    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))



root = tk.Tk()
root.title("Caesar Cipher Lab")
root.geometry("600x500")


mode_var = tk.StringVar(value="encrypt")

ttk.Label(root, text="Mode:").pack()

ttk.Radiobutton(root, text="Encrypt", variable=mode_var, value="encrypt").pack()
ttk.Radiobutton(root, text="Decrypt", variable=mode_var, value="decrypt").pack()
ttk.Radiobutton(root, text="Crack", variable=mode_var, value="crack").pack()


ttk.Label(root, text="Text:").pack()

text_input = tk.Text(root, height=6)
text_input.pack(fill="x", padx=10)


ttk.Label(root, text="Key (only encrypt/decrypt):").pack()

key_entry = ttk.Entry(root)
key_entry.pack(fill="x", padx=10)


ttk.Button(root, text="Run", command=run).pack(pady=10)


output = tk.StringVar()

ttk.Label(root, text="Result:").pack()

output_label = ttk.Label(root, textvariable=output, wraplength=550)
output_label.pack(padx=10)


if __name__ == "__main__":
    root.mainloop()
