main_dish = 24 * 3
appetizer = 12 * 2
drink = 8 * 4
service_charge = 0.90
delivery_fee = 5
total_bill = (main_dish + appetizer + drink) * service_charge + delivery_fee
amount_paid_each = total_bill / 6
print(f"Total Bill: {total_bill} (Type: {float(total_bill)})")

print(f"Amount Paid Each: {amount_paid_each}")

