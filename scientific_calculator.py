import tkinter as tk
from tkinter import messagebox
import math

class ScientificCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        entry = tk.Entry(self.master, textvariable=self.input_text, font=("Arial", 20), bd=8, insertwidth=2, width=15, borderwidth=4)
        entry.grid(row=0, column=0, columnspan=5)

        button_texts = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', 'sqrt',
            '1', '2', '3', '-', 'sin',
            '0', '.', '=', '+', 'cos',
            '(', ')', 'tan', 'log', 'asin',
            'acos', 'atan', 'exp', 'fact', 'pi',
            'e', 'round', '%'
        ]

        row_val = 1
        col_val = 0
        for text in button_texts:
            self.create_button(text, row_val, col_val)
            col_val += 1
            if col_val > 4:
                col_val = 0
                row_val += 1

    def create_button(self, text, row, col):
        button = tk.Button(self.master, text=text, padx=20, pady=20, font=("Arial", 15),
                           command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.input_text.set("")
        elif char == '=':
            try:
                result = eval(self.expression, {"__builtins__": None}, self.get_math_functions())
                self.input_text.set(result)
                self.expression = str(result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
                self.expression = ""
                self.input_text.set("")
        else:
            self.expression += char
            self.input_text.set(self.expression)

    def get_math_functions(self):
        return {
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'asin': math.asin,
            'acos': math.acos,
            'atan': math.atan,
            'exp': math.exp,
            'log': math.log10,
            'sqrt': math.sqrt,
            'fact': self.factorial,
            'pi': math.pi,
            'e': math.e,
            'round': round,
            '%': lambda x: x / 100
        }

    def factorial(self, n):
        if n < 0:
            raise ValueError("Factorial not defined for negative values")
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()
