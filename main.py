import tkinter as tk
from tkinter import messagebox
from database import add_expense, get_expenses, delete_expense

class ExpenseManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Money Management System")

        # Description Label and Entry
        self.description_label = tk.Label(root, text="Description:")
        self.description_label.grid(row=0, column=0, padx=10, pady=10)
        self.description_entry = tk.Entry(root)
        self.description_entry.grid(row=0, column=1, padx=10, pady=10)

        # Amount Label and Entry
        self.amount_label = tk.Label(root, text="Amount:")
        self.amount_label.grid(row=1, column=0, padx=10, pady=10)
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=1, column=1, padx=10, pady=10)

        # Date Label and Entry
        self.date_label = tk.Label(root, text="Date (YYYY-MM-DD):")
        self.date_label.grid(row=2, column=0, padx=10, pady=10)
        self.date_entry = tk.Entry(root)
        self.date_entry.grid(row=2, column=1, padx=10, pady=10)

        # Add Button
        self.add_button = tk.Button(root, text="Add Expense", command=self.add_expense)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Expense List
        self.expense_listbox = tk.Listbox(root, width=50)
        self.expense_listbox.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        self.expense_listbox.bind('<Delete>', self.delete_expense)

        self.load_expenses()

    def add_expense(self):
        description = self.description_entry.get()
        amount = self.amount_entry.get()
        date = self.date_entry.get()

        if not description or not amount or not date:
            messagebox.showwarning("Input Error", "All fields are required")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showwarning("Input Error", "Amount must be a number")
            return

        add_expense(description, amount, date)
        self.load_expenses()
        self.description_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)

    def load_expenses(self):
        self.expense_listbox.delete(0, tk.END)
        expenses = get_expenses()
        for expense in expenses:
            self.expense_listbox.insert(tk.END, f"{expense[0]} - {expense[1]}: ${expense[2]:.2f} on {expense[3]}")

    def delete_expense(self, event):
        selected_item = self.expense_listbox.get(tk.ACTIVE)
        if not selected_item:
            return
        expense_id = selected_item.split(' ')[0]
        delete_expense(expense_id)
        self.load_expenses()

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseManager(root)
    root.mainloop()
