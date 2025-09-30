position = input()
overtime_hours = int(input())
is_weekend = input()

hourly_rate = 0
total_pay = 0
overtime_pay = 0
bonus = 0


if position == "manager":
    hourly_rate = 35
elif position == "supervisor":
    hourly_rate = 25
elif position == "staff":
    hourly_rate = 18
else:
    hourly_rate = 0


if overtime_hours > 0:
        overtime_pay = overtime_hours * 1.5

if is_weekend == "Yes":
    bonus = overtime_hours * 5


total_pay = (hourly_rate * 8) + overtime_pay + bonus

print(hourly_rate)
print(overtime_pay)
print(total_pay)
