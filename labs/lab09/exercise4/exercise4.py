current = int(input())
previous = int(input())
consumption = current - previous

if consumption <= 20:
    water_cost = consumption * 0.57
elif consumption <= 35 and consumption > 20:
    water_cost = (20 * 0.57) + ((consumption - 20) * 1.03)
else:
    water_cost = (20 * 0.57) + (15 * 1.03) + ((consumption - 35) * 1.40)

total_bill = water_cost + 8 + 2

print(consumption)
print(water_cost)
print(total_bill)