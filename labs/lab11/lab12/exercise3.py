age_input = input()

age_count = 0
total_age = 0
average_age = 0.0

while age_input != "done":  # Condition
    age = int(age_input)
    age_count += 1
    total_age += age
    average_age = total_age / age_count
    age_input = input()

print(age_count)
print(total_age)
print(f"{average_age:.2f}")