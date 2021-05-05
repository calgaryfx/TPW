# Ex.6: Tax and Tip (p.4)

# Print the cost of the meal.
order = float(input("Cost of the meal: "))

# Compute tax and tip.
tax = order * 0.05
tip = order * 0.18

# Grand total.
total = order + tax + tip

# Receipt showing tax amount, tip amount, Grand total.
print(f"Tax: $%.2f" % tax)
print(f"Tip: $%.2f" % tip)
print(f"Grand Total: $%.2f" % total)

# Task: Program to read the cost of a meal ordred at a restaurant from the user.
# Compute the tax and tip for the meal.
# Compute the tip as 18% of the meal amount (without the tax).
# Output: Tax amount, Tip amount and Grand total for the meal including tax and
# tip. Format the output so all the values are displayed to two decimal places.

# The Python Workbook practice. Solution (p.88).
