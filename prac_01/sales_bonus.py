"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
MINIMUM_THRESHOLD = 1000
MINIMUM_BONUS = 0.1
MAXIMUM_BONUS = 0.15

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < MINIMUM_THRESHOLD:
        bonus = MINIMUM_BONUS * sales
    else:
        bonus = MAXIMUM_BONUS * sales
    print(f"Your bonus is ${bonus:.2f}.")
    sales = float(input("Enter sales: $"))
print("Goodbye.")