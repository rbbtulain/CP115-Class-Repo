membership_base = 120
personel_trainer_fee = 80
session = 6
locker_rental = 25
towel_rental = 15
one_time_register = 50

# Calculate the first month cost and monthly cost

first_month_cost = membership_base + (personel_trainer_fee * session) + locker_rental + towel_rental + one_time_register
monthly_cost = membership_base + (personel_trainer_fee * session) + locker_rental + towel_rental
all_year = (monthly_cost * 12) + first_month_cost


print(f"First Month Cost: {first_month_cost} (Type: {int(first_month_cost)})")
print(f"Monthly Cost: {monthly_cost} (Type: {int(monthly_cost)})")
