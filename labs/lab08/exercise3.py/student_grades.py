test1 = 78
test2 = 85
test3 = 92
test4 = 89
test5 = 88

print(f"Test 1: {test1} (Type: {int(test1)})")
print(f"Test 2: {test2} (Type: {int(test2)})")
print(f"Test 3: {test3} (Type: {int(test3)})")
print(f"Test 4: {test4} (Type: {int(test4)})")
print(f"Test 5: {test5} (Type: {int(test5)})")

total_points = test1 + test2 + test3 + test4 + test5
average_score = (test1 + test2 + test3 + test4 + test5) / 5

print(f"Total Points: {total_points} (Type: {int(total_points)})")
print(f"Average Score: {average_score} (Type: {float(average_score)})")


# Display the results showing each test score, total points, student average, and what percentage each test contributes to the total score.
percentage1 = (test1 / total_points) * 100
percentage2 = (test2 / total_points) * 100
percentage3 = (test3 / total_points) * 100
percentage4 = (test4 / total_points) * 100
percentage5 = (test5 / total_points) * 100

print(f"Percentage1: {percentage1}% (Type: {float(percentage1)})")
print(f"Percentage2: {percentage2}% (Type: {float(percentage2)})")
print(f"Percentage3: {percentage3}% (Type: {float(percentage3)})")
print(f"Percentage4: {percentage4}% (Type: {float(percentage4)})")
print(f"Percentage5: {percentage5}% (Type: {float(percentage5)})")



