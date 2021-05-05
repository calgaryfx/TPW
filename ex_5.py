# Ex.5: Bottle Deposits (p.4)

# Ask for amount of containers per size category.
small = int(input("Input the number of drink containers 1L or less: "))
large = int(input("Input the number of drink containers larger than 1L: "))

# Calculate refund per size category.
refund_10 = small * 0.10
refund_25 = large * 0.25
total_refund = refund_10 + refund_25

# Print refund per size category.
print(f"{small} containers 1L or less is a refund of: ${refund_10}")
print(f"{large} containers larger than 1L is a refund of: ${refund_25}")

# Print total refund.
print(f"Your total refund is: ${total_refund}")

# Task: Recycle deposit for 1 litre or less = $0.10.
# Recycle deposit for greater than 1 litre = $0.25 deposit.
# Count the number of containers of each size from the user.
# Compute and display the refund to the user. Format with a dollar sign and always
# display two decimal places.
# The Python Workbook practice. Solution (p.88).
