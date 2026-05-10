import tkinter as tk
from tkinter import ttk, messagebox

from cipher.text_utils import normalize_text, group_by_five
from cipher.caesar import encrypt, decrypt
from cipher.cracker import crack


def paste_text(event):
    widget = event.widget
    try:
        text = widget.clipboard_get()
        widget.insert(tk.INSERT, text)
    except tk.TclError:
        pass
    return "break"


def on_mode_change(*_):
    if mode_var.get() == "crack":
        key_row.pack_forget()
    else:
        key_row.pack(fill="x", pady=(0, 8), before=btn_row)


def run():
    text = text_input.get("1.0", tk.END).strip()
    if not text:
        messagebox.showerror("Ошибка", "Введите текст")
        return

    text = normalize_text(text)
    if not text:
        messagebox.showerror("Ошибка", "Текст не содержит допустимых символов")
        return

    mode = mode_var.get()

    try:
        if mode in ("encrypt", "decrypt"):
            raw = key_entry.get().strip()
            if not raw:
                messagebox.showerror("Ошибка", "Введите ключ")
                return
            key = int(raw)
            result = encrypt(text, key) if mode == "encrypt" else decrypt(text, key)
            set_output(group_by_five(result))

        elif mode == "crack":
            key, result = crack(text)
            set_output(f"Наиболее вероятный ключ: {key}\n\n{group_by_five(result)}")

    except ValueError as e:
        msg = str(e)
        if "invalid literal" in msg:
            msg = "Ключ должен быть целым числом"
        messagebox.showerror("Ошибка", msg)


def set_output(text: str):
    result_box.config(state="normal")
    result_box.delete("1.0", tk.END)
    result_box.insert("1.0", text)
    result_box.config(state="disabled")


def clear_all():
    text_input.delete("1.0", tk.END)
    key_entry.delete(0, tk.END)
    set_output("")


root = tk.Tk()
root.title("Шифр Цезаря")
root.geometry("540x520")
root.resizable(False, False)

pad = dict(padx=16)

ttk.Label(root, text="Режим:").pack(anchor="w", pady=(14, 2), **pad)

mode_frame = ttk.Frame(root)
mode_frame.pack(anchor="w", **pad)

mode_var = tk.StringVar(value="encrypt")
mode_var.trace_add("write", on_mode_change)

ttk.Radiobutton(mode_frame, text="Зашифровать", variable=mode_var, value="encrypt").pack(side="left", padx=(0, 12))
ttk.Radiobutton(mode_frame, text="Расшифровать", variable=mode_var, value="decrypt").pack(side="left", padx=(0, 12))
ttk.Radiobutton(mode_frame, text="Взломать",     variable=mode_var, value="crack").pack(side="left")

ttk.Separator(root, orient="horizontal").pack(fill="x", pady=10, **pad)

ttk.Label(root, text="Исходный текст:").pack(anchor="w", **pad)
text_input = tk.Text(root, height=7, font=("Courier New", 10), wrap="word")
text_input.pack(fill="x", pady=(2, 10), **pad)
text_input.bind("<Control-v>", paste_text)
text_input.bind("<Control-V>", paste_text)

key_row = ttk.Frame(root)
key_row.pack(fill="x", pady=(0, 8), **pad)
ttk.Label(key_row, text="Ключ:").pack(side="left", padx=(0, 8))
key_entry = ttk.Entry(key_row, width=10)
key_entry.pack(side="left")

btn_row = ttk.Frame(root)
btn_row.pack(fill="x", pady=(0, 10), **pad)
ttk.Button(btn_row, text="Выполнить", command=run).pack(side="left", padx=(0, 8))
ttk.Button(btn_row, text="Очистить",  command=clear_all).pack(side="left")

ttk.Separator(root, orient="horizontal").pack(fill="x", pady=(0, 10), **pad)

ttk.Label(root, text="Результат:").pack(anchor="w", **pad)
result_box = tk.Text(root, height=7, font=("Courier New", 10), wrap="word", state="disabled")
result_box.pack(fill="x", pady=(2, 10), **pad)


if __name__ == "__main__":
    root.mainloop()
