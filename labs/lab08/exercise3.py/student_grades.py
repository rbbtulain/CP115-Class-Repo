test1 = 78
test2 = 85
test3 = 92
test4 = 67
test5 = 88

total_points = test1 + test2 + test3 + test4 + test5
average_score = (test1 + test2 + test3 + test4 + test5) / 5

print(f"Average Score: {average_score} (Type: {float(average_score)})")
print(f"Total Points: {total_points} (Type: {int(total_points)})")

# Display the results showing each test score, total points, student average, and what percentage each test contributes to the total score.
percentage = (total_points / 500) * 100
print(f"Percentage: {percentage}% (Type: {float(percentage)})")

