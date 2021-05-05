# Ex.5: Bottle Deposits (p.4) Authors' solution (p.88).

# Compute the refund amount for a collection of bottles.
LESS_DEPOSIT = 0.10
MORE_DEPOSIT = 0.25

# Read input from the user:
less = int(input("How many containers 1 litre or less do you have?"))
more = int(input("How many containers more than 1 litre do you have?"))

# Compute the refund amount.
refund = less * LESS_DEPOSIT + more * MORE_DEPOSIT

# Display the result
print("Your total refund will be $%.2f." % refund)

# The %.2f format specifier indicates that a value should be formatted as a floating
# point number with 2 digits to the right of the decimal point.
