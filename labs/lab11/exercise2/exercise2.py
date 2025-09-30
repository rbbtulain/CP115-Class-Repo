num_days = int(input())              # Number of days to process
danger_threshold = float(input())    # Danger temperature threshold

danger_days = 0
total_temp = 0

for i in range(num_days):
    temp = float(input())
    if temp > danger_threshold:
        danger_days += 1
    
    total_temp += temp

average_temp = total_temp / num_days

print(danger_days)
print(f"{average_temp:.1f}")
