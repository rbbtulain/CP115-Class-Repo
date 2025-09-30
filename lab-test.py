# The program calculates the amount to be paid based on monthly usage.
# Programmer: Ain

monthly_usage = int(input("Enter monthly usage: "))

amount_paid = 0

if monthly_usage < 50:
    amount_paid = monthly_usage
elif monthly_usage <= 100 and monthly_usage >= 50:
    amount_paid = monthly_usage - (monthly_usage * 0.05)
elif monthly_usage > 100:
    amount_paid = monthly_usage - (monthly_usage * 0.20)

print (amount_paid)

