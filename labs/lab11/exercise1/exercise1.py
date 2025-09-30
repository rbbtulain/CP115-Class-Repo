num_rounds = int(input())

# Initialize total score and counter
total_score = 0
rounds_processed = 0

# Process each round
for i in range(num_rounds):
    # Get score for this round
    round_score = float(input())

    # Check if bonus applies
    if round_score > 100:
        bonus = 0.20 * round_score
        round_score += bonus

    # Add to total score
    total_score += round_score
    rounds_processed += 1

# Output final total score and number of rounds processed
print(f"{total_score:.1f}")
print(rounds_processed)
