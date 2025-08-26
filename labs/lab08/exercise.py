# Same numbers, different brackets = different results
without_brackets = 5 + 3 * 2 ** 2
with_brackets = (5 + 3) * 2 ** 2
different_brackets = 5 + (3 * 2) ** 2
print(f"5 + 3 * 2 ** 2 = {without_brackets}")
print(f"(5 + 3) * 2 ** 2 = {with_brackets}")
print(f"5 + (3 * 2) ** 2 = {different_brackets}")