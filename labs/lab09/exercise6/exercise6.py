position = input()
overtime_hours = int(input())
is_weekend = input()   # expected "yes" or "no"

# Step 1: Base rates
base_rates = {
    "manager": 30,
    "supervisor": 20,
    "staff": 15,
    "intern": 8
}

# Get base hourly rate
base_rate = base_rates[position]

# Step 2: Overtime calculation
if overtime_hours <= 8:
    overtime_pay = overtime_hours * (1.5 * base_rate)
else:
    overtime_pay = (8 * 1.5 * base_rate) + ((overtime_hours - 8) * (2.0 * base_rate))

# Step 3: Weekend bonus
if is_weekend == "yes":
    overtime_pay += overtime_hours * 5

# Step 4: Output
print(overtime_pay)
