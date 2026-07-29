# ============================================
# Personal Finance Tracker
# Author: Doyin Oyedijo
# Description: Analyzes transactions made by a user.
# ============================================

import pandas as pd
from datetime import datetime
import csv

# ---- STEP 1: Create the users Bank account ----

class PersonAccount(): #PersonAccount class
  def __init__(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname
    self.incomes = {}
    self.expenses = {}

  def account_balance(self): #Calculates the account balance by subtracting expenses from income
    return self.total_income() - self.total_expenses()

  def add_income(self, description, amount): #Adds additional income from user
    self.incomes[description] = amount

  def add_expense(self, description, amount):
    self.expenses[description] = amount

  def total_income(self): #Adds all income amounts
    incometotal = 0
    for income in self.incomes.values():
      incometotal += income
    return incometotal

  def total_expenses(self): #Adds all expense amounts
    expensetotal = 0
    for expense in self.expenses.values():
      expensetotal += expense

    return expensetotal

  def account_info(self): #Compiles all information about the users information
    return (
        f'{self.firstname} {self.lastname}\n'
        f'Total Income: {self.total_income()}\n'
        f'Total Expenses: {self.total_expenses()}\n'
        f'Account Balance: {self.account_balance()}'
    )


# ---- STEP 2: Compile the Transactions----

class Transactions(PersonAccount):
  def __init__(self, firstname, lastname):
    super().__init__(firstname, lastname)
    self.transactionhistory = []

  def add_income(self, description, amount, incomesource, date = None):
    super().add_income(description, amount)
    if date == None:
      date = datetime.now()
    self.transactionhistory.append({'type': 'income', 'Transactiontype': incomesource, 'Amount': amount, 'Description': description, 'Date': date})


  def add_expense(self, description, amount, expensesource, date= None):
    super().add_expense(description, amount)
    if date == None:
      date = datetime.now()
    self.transactionhistory.append({'type': 'expense', 'Transactiontype': expensesource, 'Amount': amount, 'Description': description, 'Date': date})

  def save_transactions(self):
      df = pd.DataFrame(self.transactionhistory)
      df.to_csv('transactions.csv', index=False)

  def load_transactions(self):
    df = pd.read_csv('transactions.csv')
    self.transactionhistory = df.to_dict('records')

    income_rows = df[df['type'] == 'income']
    for _, row in income_rows.iterrows():
      self.incomes[row['Description']] = row['Amount']

    expense_rows = df[df['type'] == 'expense']
    for _, row in expense_rows.iterrows():
      self.expenses[row['Description']] = row['Amount']

# ---- STEP 3: Clean and Analyze Data ----

def analyze(account):
    df = pd.DataFrame(account.transactionhistory)
    
    print("=== ACCOUNT SUMMARY ===")
    print(f"Account holder: {account.firstname} {account.lastname}")
    print(f"Total income: £{account.total_income():,.2f}")
    print(f"Total expenses: £{account.total_expenses():,.2f}")
    print(f"Account balance: £{account.account_balance():,.2f}")
    print(f"Savings rate: {(account.account_balance() / account.total_income() * 100):.1f}%")

    print("\n=== INCOME BREAKDOWN ===")
    income_df = df[df['type'] == 'income']
    print(income_df.groupby('Transactiontype')['Amount'].sum().sort_values(ascending=False))

    print("\n=== EXPENSE BREAKDOWN ===")
    expense_df = df[df['type'] == 'expense']
    print(expense_df.groupby('Transactiontype')['Amount'].sum().sort_values(ascending=False))

    print("\n=== BIGGEST EXPENSE ===")
    biggest = df[df['type'] == 'expense'].sort_values('Amount', ascending=False).iloc[0]
    print(f"{biggest['Description']} — £{biggest['Amount']:,.2f}")

    return df

def save(account):
    account.save_transactions()
    print("Transactions saved to transactions.csv")

# ---- MAIN ----
account = Transactions('Tryea', 'Vivet')
account.add_income('YouTube', 50000, 'Content')
account.add_income('Python freelance', 3000, 'Freelance')
account.add_expense('Rent', 2000, 'Housing')
account.add_expense('Groceries', 500, 'Food')
account.add_expense('Internet', 100, 'Utilities')

df = analyze(account)
save(account)
