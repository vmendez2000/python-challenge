import csv
import os

# Files to load and output 
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = []
net_total = 0
net_change_list = []
previous_profit = None
months = []  # Keep track of months

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Process each row of data
    for row in reader:
        # Track the total months
        months.append(row[0])  # Assuming the first column is the date
        total_months.append(row[0])  # Assuming the first column is the date
        current_profit = int(row[1])  # Assuming the second column is Profit/Losses
        net_total += current_profit

        # Track the net change
        if previous_profit is not None:
            net_change = current_profit - previous_profit
            net_change_list.append(net_change)
        previous_profit = current_profit

# Calculate the total number of months
total_months = len(months)

# Calculate the average net change across the months
average_change = sum(net_change_list) / len(net_change_list) if net_change_list else 0

# Calculate the greatest increase and decrease in profits
greatest_increase = max(net_change_list) if net_change_list else 0
greatest_decrease = min(net_change_list) if net_change_list else 0

# Find the months corresponding to the greatest increase and decrease
greatest_increase_month = months[net_change_list.index(greatest_increase) + 1] if net_change_list else ""
greatest_decrease_month = months[net_change_list.index(greatest_decrease) + 1] if net_change_list else ""

# Generate the output summary
with open(file_to_output, 'w') as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("----------------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${net_total}\n")
    txt_file.write(f"Average Change: ${average_change:.2f}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")

# Print the output
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")
