import tkinter as tk
from calculator_logic import Calculator

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.calc = Calculator()

        # Entry display
        self.display = tk.Entry(master, font=("Arial", 24), bd=5, relief="sunken", justify="right")
        self.display.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        # Buttons layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('C', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('M+', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('MR', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3), ('MC', 4, 4),
            ('√', 5, 0), ('x^y', 5, 1), ('x!', 5, 2), ('%', 5, 3)
        ]

        for (text, row, col) in buttons:
            b = tk.Button(master, text=text, width=5, height=2, font=("Arial", 18),
                          command=lambda t=text: self.on_button_click(t))
            b.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, char):
        if char in '0123456789.':
            self.display.insert(tk.END, char)
        elif char in '+-*/':
            self.display.insert(tk.END, f' {char} ')
        elif char == 'C':
            self.display.delete(0, tk.END)
        elif char == '=':
            try:
                expr = self.display.get()
                # Split expression safely
                parts = expr.split()
                x = float(parts[0])
                op = parts[1]
                y = float(parts[2])
                if op == '+':
                    result = self.calc.add(x, y)
                elif op == '-':
                    result = self.calc.subtract(x, y)
                elif op == '*':
                    result = self.calc.multiply(x, y)
                elif op == '/':
                    result = self.calc.divide(x, y)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif char == '√':
            x = float(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, str(self.calc.sqrt(x)))
        elif char == 'x^y':
            x = float(self.display.get())
            y = float(input("Enter exponent y: "))  
            self.display.delete(0, tk.END)
            self.display.insert(0, str(self.calc.power(x, y)))
        elif char == 'x!':
            x = int(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, str(self.calc.factorial(x)))
        elif char == '%':
            x = float(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, str(self.calc.percentage(x)))
        elif char == 'M+':
            self.calc.store_memory()
        elif char == 'MR':
            self.display.delete(0, tk.END)
            self.display.insert(0, str(self.calc.recall_memory()))
        elif char == 'MC':
            self.calc.clear_memory()

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
