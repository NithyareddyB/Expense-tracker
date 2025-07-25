### Personal Expense Tracker

This GitHub repository contains a personal expense tracker application with both a command-line interface (CLI) and a web-based dashboard. The CLI allows users to add and view expenses, while the dashboard provides a visual overview of spending habits.

### Features

* **Add Expenses (CLI):** Quickly add new expenses with details like date, category, description, and amount.
* **View Expenses (CLI):** See a list of all recorded expenses and the total amount spent.
* **Interactive Dashboard:** Visualize your spending patterns with charts and graphs.
* **Category-wise Analysis:** Understand where your money is going with breakdowns by category.
* **Time-series Spending:** Track your expenses over time to identify trends.
* **Data Persistence:** All expense data is saved to a CSV file.

### Files

* `expense_tracker.py`: This Python script provides the command-line interface for adding and viewing expenses.
* `dashboard.py`: This Python script powers the interactive web-based expense dashboard using Streamlit.
* `expenses.csv`: (Generated after first use) This CSV file stores all your expense data.

## 🔗 Live Demo

Check out the live deployed dashboard on Streamlit:  
👉 [Expense Tracker Dashboard](https://expense-tracker-mclbxi2s3ijsi7ecgmkf5a.streamlit.app/)

### How to Use

**1. Clone the Repository**

```bash
git clone https://github.com/NithyareddyB/Expense-tracker.git
cd Expense-tracker
```
**2. Install Dependencies**
Install Python on the system. Then, install the required libraries:

```bash

pip install pandas streamlit plotly
```
**3. Using the Command-Line Interface (CLI)**
To add and view expenses, run the expense_tracker.py script:

```bash

python expense_tracker.py
```
Follow the on-screen prompts to choose options like adding a new expense or viewing existing ones.

**4. Using the Web Dashboard**

To visualize the expenses, run the dashboard.py script using Streamlit:

```bash

streamlit run dashboard.py
```
This will open the expense dashboard in your web browser. If no expenses are added using the CLI, the dashboard will show a warning because there is nothing to display.

### 📝Note on Data
* This repository includes a sample expenses.csv file with dummy data.
* When you run the CLI (expense_tracker.py), it will append your own data to this file.
* You can edit or delete the file to start fresh.
* All your changes are local
