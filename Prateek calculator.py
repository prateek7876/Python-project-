import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Calculator")

        self.expression = ""

        # Entry widget to display the expression
        self.entry = tk.Entry(master, width=16, font=('Arial', 24), borderwidth=2, relief='ridge')
        self.entry.grid(row=0, column=0, columnspan=4)

        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # Create buttons and place them in the grid
        row_val = 1
        col_val = 0
        for button in buttons:
            tk.Button(master, text=button, width=5, height=2, font=('Arial', 18),
                      command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Clear button
        tk.Button(master, text='C', width=5, height=2, font=('Arial', 18),
                  command=self.clear).grid(row=row_val, column=0)

    def on_button_click(self, char):
        if char == '=':
            try:
                # Evaluate the expression and display the result
                self.expression = str(eval(self.expression))
            except Exception as e:
                self.expression = "Error"
        else:
            self.expression += str(char)
        self.update_entry()

    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def clear(self):
        self.expression = ""
        self.update_entry()

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()