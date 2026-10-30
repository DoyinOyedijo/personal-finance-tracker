# Personal Finance Tracker

Python income and expense tracker with OOP and CSV persistence

## What it does
- Accepts income and expense transactions with a description, amount, and source
- Calculates total income, total expenses, account balance, and savings rate
- Breaks down spending and earnings by category
- Exports all transaction data to a CSV file for persistent storage
- Loads previous transactions from a saved file to rebuild account history

## Technologies
- Python
- pandas
- OOP (inheritance)
- File handling (CSV)
- datetime

## How to run
```
pip install pandas
python PersonalFinanceTracker.py
```

## Key features
- `PersonAccount` base class handles core account logic
- `Transactions` child class extends it with transaction history and file persistence
- Save and load transactions across sessions using CSV
- Full financial summary including savings rate and category breakdowns

## Author
Doyin Oyedijo — [github.com/DoyinOyedijo](https://github.com/DoyinOyedijo)
