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

print(f"Test 1: {test1} (Type: {int(test1)})")
print(f"Test 2: {test2} (Type: {int(test2)})")
print(f"Test 3: {test3} (Type: {int(test3)})")
print(f"Test 4: {test4} (Type: {int(test4)})")
print(f"Test 5: {test5} (Type: {int(test5)})")
print(f"")
