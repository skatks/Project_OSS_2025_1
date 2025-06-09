import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("공학용 계산기")
        self.root.geometry("320x600")

        self.expr = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 일반 계산기 버튼
        buttons = [
            ['(', ')', '$', ' '],
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=']
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

        # 공학용 계산 버튼
        sci_buttons = [
            ['sin', 'cos', 'tan'],
            ['log', 'ln', '√'],
            ['^', 'pi', 'e']
        ]

        for row in sci_buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for func in row:
                btn = tk.Button(
                    frame,
                    text=func,
                    font=("Arial", 16),
                    command=lambda ch=func: self.insert_scientific(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

    def on_click(self, char):
        if char == 'C':
            self.expr = ""

        elif char == '$':
            if self.expr:
                try:
                    amount = float(self.expr)
                    self.expr = f"{amount / 1350:.2f}달러"
                except ValueError:
                    self.expr = "에러"
        elif char == '=':
            try:
                result = eval(self.expr, {"__builtins__": None}, {"math": math})
                self.expr = str(result)
            except Exception:
                self.expr = "에러"
        else:
            self.expr += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expr)

    def insert_scientific(self, func):
        if func == 'sin':
            self.expr += 'math.sin(math.radians('
        elif func == 'cos':
            self.expr += 'math.cos(math.radians('
        elif func == 'tan':
            self.expr += 'math.tan(math.radians('
        elif func == 'log':
            self.expr += 'math.log10('
        elif func == 'ln':
            self.expr += 'math.log('
        elif func == '√':
            self.expr += 'math.sqrt('
        elif func == '^':
            self.expr += '**'
        elif func == 'pi':
            self.expr += 'math.pi'
        elif func == 'e':
            self.expr += 'math.e'

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expr)

# 실행
if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
