main_course = input()
drink = input()
dessert = input()
customer_age = int(input())

# TODO: Your code here
if main_course == "chicken":
    price = 10
if main_course == "beef":
    price = 12
if main_course == "fish":
    price = 11

if drink == "soft_drink":
    price = 2
if drink == "coffee":
    price = 3

if dessert == "ice_cream":
    price = 4
if dessert == "cake":
    price = 5

final_bill = (price * main_course) + ( price * drink) + (price * dessert)

if customer_age < 18:
    final_bill = final_bill - (final_bill * 0.10)

if customer_age >= 60:
    final_bill = final_bill - (final_bill * 0.15)


print(f"{final_bill:.2f}")