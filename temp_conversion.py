import re
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def is_decimal(string):
    pattern = re.compile(r'^[-+]?(\d+)?\.?(\d+)?$')
    return bool(pattern.match(string))


def convert_temperature():
    temperature = temp_var.get()
    temperature = temp_var.get()
    scale = scale_var.get()

    if temperature == '' or temperature == '.':
        temperature = '0'

    if not is_decimal(temperature):
        messagebox.showerror("Ошибка", "Неверный формат ввода.\nПожалуйста, введите число.")
        return

    if len(temperature.split('.')[0]) > 8:
        messagebox.showerror("Ошибка", "Слишком длинное число.")
        return

    temperature = float(temperature)
    if scale == "C":
        celsius = temperature
        fahrenheit = (celsius * 9/5) + 32
        kelvin = celsius + 273.15
    elif scale == "F":
        fahrenheit = temperature
        celsius = (fahrenheit - 32) * 5/9
        kelvin = celsius + 273.15
    elif scale == "K":
        kelvin = temperature
        celsius = kelvin - 273.15
        fahrenheit = celsius * 9/5 + 32

    if kelvin < 0.0:
        messagebox.showerror("Ошибка", "Температура не может быть ниже абсолютного нуля.")
    else:
        celsius_label.config(text=f"°C = {celsius:.2f}")
        fahrenheit_label.config(text=f"°F = {fahrenheit:.2f}")
        kelvin_label.config(text=f" K = {kelvin:.2f}")


if __name__ == '__main__':

    root = tk.Tk()

    root.title("Конвертер температур")
    root.geometry("300x200")
    root.resizable(False, False)


    temp_var = tk.StringVar(value="0")
    scale_var = tk.StringVar(value='C')


    style = ttk.Style()
    style.configure('TButton', font=("Arial", 12))


    input_frame = ttk.Frame(root)
    input_frame.pack(pady=10)

    temp_label = ttk.Label(input_frame, text="Температура", padding=5, font=("Arial", 12))
    temp_label.grid(row=0, column=0)

    temp_entry = ttk.Entry(input_frame, width=9, textvariable=temp_var, font=("Arial", 12))
    temp_entry.grid(row=0, column=1, padx=5)

    scale_drop = ttk.Combobox(input_frame, width=4, textvariable=scale_var, values=['C','F','K'], font=("Arial", 12))
    scale_drop.grid(row=0, column=2, padx=5)

    # Button
    convert_button = ttk.Button(root, text="Конвертировать", width=20, command=convert_temperature)
    convert_button.pack(padx=5, pady=8)

    # Output
    celsius_label = ttk.Label(root, text="°C = ", font=("Arial", 12))
    celsius_label.pack(padx=50, pady=4, anchor=tk.W)

    fahrenheit_label = ttk.Label(root, text="°F = ", font=("Arial", 12))
    fahrenheit_label.pack(padx=50, pady=4, anchor=tk.W)

    kelvin_label = ttk.Label(root, text=" K = ", font=("Arial", 12))
    kelvin_label.pack(padx=50, pady=4, anchor=tk.W)


    root.mainloop()

