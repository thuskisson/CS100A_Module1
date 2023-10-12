# Bill Total
bill = input("Please enter your bill amount ")
bill =float(bill)

# Create a function

# Tip Percentages of the Bill Total
tip_10_percent = 0.10
tip_15_percent = 0.15
tip_20_percent = 0.20
tip_25_percent = 0.25

# Calculate the tip and total amount paid assuming different tip amounts
tip_10 = (bill * tip_10_percent)
total_10 = (bill + tip_10)

tip_15 = (bill * tip_15_percent)
total_15 = (bill + tip_15)

tip_20 = (bill * tip_20_percent)
total_20 = (bill + tip_20)

tip_25 = (bill * tip_25_percent)
total_25 = (bill + tip_25)

# Print the tip totals and the bill totals based on tip amounts
print(f"10% Tip: ${tip_10: .2f}, Total Bill: ${total_10: .2f}")
print(f"15% Tip: ${tip_15: .2f}, Total Bill: ${total_15: .2f}")
print(f"20% Tip: ${tip_20: .2f}, Total Bill: ${total_20: .2f}")
print(f"25% Tip: ${tip_25: .2f}, Total Bill: ${total_25: .2f}")

# Tips are rounded to two decimal places