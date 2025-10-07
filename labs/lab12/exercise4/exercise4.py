score_input = input()

passing_count = 0
failing_count = 0
total_count = 0
pass_rate = 0.0

while score_input != "end" and -1 and 0:  # Condition
    score = float(score_input)
    total_count += 1
    if score >= 60:
        passing_count += 1
    if score < 60:
        failing_count += 1
    score_input = input()
    if total_count > 0:
        pass_rate = (passing_count / total_count) * 100

print(passing_count)
print(failing_count)
print(f"{pass_rate:.2f}")