import csv
import os
from datetime import datetime

def add_expense():

    print("\n--- Add New Expense ---")
    
    # Get user input
    date = input("Date (YYYY-MM-DD) or press enter for today: ")
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    
    category = input("Category (Food/Transport/Bills/Other): ").strip()
    if not category:
        category = "Other"
    
    description = input("Description: ").strip()
    amount = float(input("Amount: $"))
    
    # Save to CSV
    with open('expenses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])
    
    print(f"Added: ${amount} for {category}")

def view_expenses():
    print("\n--- Your Expenses ---")
    
    if not os.path.exists('expenses.csv'):
        print("No expenses found!")
        return
    
    total = 0
    with open('expenses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 4:
                date, category, desc, amount = row
                total += float(amount)
                print(f"{date} | {category:12} | ${float(amount):6.2f} | {desc}")
    
    print(f"\nTotal spent: ${total:.2f}")

def create_csv_header():
    if not os.path.exists('expenses.csv'):
        with open('expenses.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['date', 'category', 'description', 'amount'])

def main():
    create_csv_header()
    
    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1. Add expense")
        print("2. View expenses") 
        print("3. Exit")
        
        choice = input("\nChoose option: ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()