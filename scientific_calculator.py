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
        entry = tk.Entry(
            self.master,
            textvariable=self.input_text,
            font=("Digital-7", 30),
            bd=8,
            insertwidth=2,
            width=18,
            borderwidth=4,
            justify="right",
            fg="white",
            bg="black",
            highlightbackground="black",
            highlightthickness=1,
        )
        entry.grid(row=0, column=0, columnspan=5, pady=10, padx=5)

        buttons = [
            ["C", "(", ")", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            [".", "0", "π", "√"],
        ]
        
        scientific_buttons = [
            ["sin", "cos", "tan", "log"],
            ["asin", "acos", "atan", "exp"],
            ["fact", "%", "e", "="],
        ]

        for row, button_row in enumerate(buttons):
            for col, text in enumerate(button_row):
                self.create_button(
                    text,
                    row + 1,
                    col,
                    colspan=1,
                    bg_color=self.get_button_color(text),
                )

        for row, button_row in enumerate(scientific_buttons, start=6):
            for col, text in enumerate(button_row):
                self.create_button(
                    text,
                    row + 1,
                    col,
                    colspan=1,
                    bg_color=self.get_button_color(text),
                )

        for i in range(7):
            self.master.grid_rowconfigure(i, weight=1)
        for i in range(5):
            self.master.grid_columnconfigure(i, weight=1)

    def create_button(self, text, row, col, bg_color="#2ecc71", colspan=1, sticky="nsew"):
        button = tk.Button(
            self.master,
            text=text,
            padx=20,
            pady=20,
            font=("Roboto Mono", 15),
            bg=bg_color,
            fg="#ffffff",
            command=lambda: self.on_button_click(text),
        )
        button.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5, sticky=sticky)


    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
            self.input_text.set("")
        elif char == "=":
            try:
                expression = self.expression.replace("×", "*").replace("÷", "/").replace("π", "pi")
                result = eval(expression, {"__builtins__": None}, self.get_math_functions())
                self.input_text.set(result)
                self.expression = str(result)
            except Exception:
                messagebox.showerror("Error", "Invalid Input")
                self.expression = ""
                self.input_text.set("")
        elif char in ["√", "fact", "sin", "cos", "tan", "asin", "acos", "atan", "log", "exp"]:
            self.expression += f"{char}("
            self.input_text.set(self.expression)
        else:
            self.expression += char
            self.input_text.set(self.expression)

    def get_button_color(self, text):
        if text in ["+", "-", "×", "÷", "√"]:
            return "#3498db"
        elif text in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".",  "π", "(", ")"]:
            return "#2ecc71"
        if text in ["C", "="]:
            return "#e74c3c"
        if text in ["%", "fact", "sin", "cos", "tan", "asin", "acos", "atan", "log", "exp", "e"]:
            return "#9b59b6"

    def get_math_functions(self):
        return {
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "asin": math.asin,
            "acos": math.acos,
            "atan": math.atan,
            "exp": math.exp,
            "log": math.log10,
            "√": math.sqrt,
            "fact": self.factorial,
            "pi": math.pi,
            "e": math.e,
            "%": lambda x: x / 100,
        }

    def factorial(self, n):
        if n < 0:
            raise ValueError("Factorial not defined for negative values")
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)


if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)
    root.geometry("410x766")
    calculator = ScientificCalculator(root)
    root.configure(bg="#34495e")
    root.mainloop()
