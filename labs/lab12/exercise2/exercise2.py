score = float(input())

average_score = 0.0
score_count = 0
total_score = 0.0

while score > 0 and score < 100:  # Condition
    score_count += 1
    total_score += score
    score = float(input())

print(score_count)
print(total_score)
print(f"{average_score:.2f}")