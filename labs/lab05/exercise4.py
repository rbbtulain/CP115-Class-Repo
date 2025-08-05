item_name = input("Item Name:")
item_price = float(input("Item Price:"))
item_quantity = int(input("Item Quantity:"))

subtotal = item_price * item_quantity
tax_amount = 0.06 * subtotal
total_cost = subtotal + tax_amount

print("Subtotal:" + str(subtotal))
print("Tax Ammount:" + str(tax_amount))
print("Total Cost:" + str(total_cost))
