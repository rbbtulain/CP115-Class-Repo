employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()

# Step 1: Calculate Overtime Pay and Total Income
# Overtime is paid at a flat rate of RM35 per hour.
overtime_pay = overtime_hours * 35
total_income = base_salary + overtime_pay

# Step 2: Determine the correct tax rate based on status and income
tax_rate = 0.0 # Initialize tax_rate to 0.0

if tax_status.lower() == "single":
    if total_income >= 5000:
        tax_rate = 0.22
    else:
        tax_rate = 0.18
elif tax_status.lower() == "married":
    if total_income >= 6000:
        tax_rate = 0.20
    else:
        tax_rate = 0.15
elif tax_status.lower() == "head":
    if total_income >= 5500:
        tax_rate = 0.25
    else:
        tax_rate = 0.19
# If the status is invalid, tax_rate remains 0.0

# Step 3: Calculate deductions and final net salary
# Statutory deductions are calculated from the total income.
epf_deduction = total_income * 0.11
socso_deduction = total_income * 0.005

# Income tax is calculated on the income *after* statutory deductions.
taxable_income = total_income - epf_deduction - socso_deduction
tax_amount = taxable_income * tax_rate

# Net salary is the total income minus all deductions.
net_salary = total_income - epf_deduction - socso_deduction - tax_amount

# Final Output
print(employee_name)
print(f"{int(tax_rate * 100)}%")
print(net_salary)