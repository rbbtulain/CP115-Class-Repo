main_course = input()
drink = input()
dessert = input()
customer_age = int(input())
price = 0


# TODO: Your code here
if main_course == "chicken":
    menu_price = 10
elif main_course == "beef":
    menu_price = 12
elif main_course == "fish":
    menu_price = 11

if drink == "soft_drink":
    drink_price = 2
if drink == "coffee":
    drink_price = 3

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