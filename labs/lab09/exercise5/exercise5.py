# /labs/lab09/exercise5/exercise5.py

main_course = input()
drink = input()
dessert = input()
customer_age = int(input())

# Menu prices
main_course_prices = {
    "chicken": 10,
    "beef": 12,
    "fish": 11
}

drink_prices = {
    "soft_drink": 2,
    "coffee": 3
}

dessert_prices = {
    "ice_cream": 4,
    "cake": 5
}

# Step 1: Get item prices
total_food = 0
if main_course in main_course_prices:
    total_food += main_course_prices[main_course]

if drink in drink_prices:
    total_food += drink_prices[drink]

if dessert in dessert_prices:
    total_food += dessert_prices[dessert]

# Step 2: Add service charge (10%)
bill_with_service = total_food * 1.10

# Step 3: Apply discounts
if customer_age > 60:  # Senior citizen discount
    final_bill = bill_with_service * 0.85
elif customer_age < 18:  # Student discount
    final_bill = bill_with_service * 0.90
else:
    final_bill = bill_with_service

# Step 4: Output
print(f"{final_bill:.2f}")
