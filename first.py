import pandas as pd
import tkinter as tk
from tkinter import filedialog

# Function to select a file using a file dialog
def select_file(prompt):
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(title=prompt, filetypes=[("CSV Files", "*.csv")])
    if not file_path:
        print("No file selected.")
        exit(1)
    return file_path

# Select the tally file
tally_file = select_file("Select the Tally Balance CSV File")

# Load the tally CSV file
tally_data = pd.read_csv(tally_file)

# Print the column names to debug
print("Tally Data Columns:", tally_data.columns)

# Ensure necessary columns exist
required_columns = ['InvoiceNumber', 'Debtor', 'Creditor']
if not all(col in tally_data.columns for col in required_columns):
    print("Error: One or more required columns are missing in the tally data.")
    exit(1)

# Calculate total balance of the tally data
total_debtor_tally = tally_data['Debtor'].sum()
total_creditor_tally = tally_data['Creditor'].sum()

print(f"Total Debtor Balance in Tally Data: {total_debtor_tally}")
print(f"Total Creditor Balance in Tally Data: {total_creditor_tally}")

# Prompt for actual total balance
actual_total_balance = float(input("Enter the actual total balance: "))

# Compare the actual total balance with the sum of debtor and creditor balances from tally data
total_balance_tally = total_debtor_tally + total_creditor_tally

balance_difference = total_balance_tally - actual_total_balance

print(f"Total Balance from Tally Data: {total_balance_tally}")
print(f"Actual Total Balance: {actual_total_balance}")
print(f"Balance Difference: {balance_difference}")

# Create a dataframe for comparison
comparison_data = {
    'Total Debtor Balance in Tally Data': [total_debtor_tally],
    'Total Creditor Balance in Tally Data': [total_creditor_tally],
    'Total Balance from Tally Data': [total_balance_tally],
    'Actual Total Balance': [actual_total_balance],
    'Balance Difference': [balance_difference]
}

comparison_df = pd.DataFrame(comparison_data)

# Save the comparison to a CSV file
comparison_df.to_csv('comparison_summary.csv', index=False)

print("Comparison summary saved to 'comparison_summary.csv'.")
