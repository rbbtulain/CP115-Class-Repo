day_type = input()
show_time = int(input())
customer_type = input()
is_student = input()

# Set base price
if day_type == "Weekend":
    if customer_type == "Adult":
        base_price = 18
    elif customer_type == "Child":
        base_price = 12
    elif customer_type == "Senior":
        base_price = 15
    else:
        base_price = 0
else:  # Weekday
    if customer_type == "Adult":
        base_price = 15
    elif customer_type == "Child":
        base_price = 10
    elif customer_type == "Senior":
        base_price = 12
    else:
        base_price = 0

final_price = base_price

# Evening surcharge (after 6pm)
if show_time > 18:
    final_price = base_price + 3

# Student discount (only on weekdays)
if day_type == "Weekday" and is_student == "Yes":
    final_price = final_price - (final_price *0.10)

print(base_price)
print(final_price)