yardLength = float(input())
yardWidth = float(input())
houseLength = float(input())
houseWidth = float(input())
houseArea = houseLength * houseWidth
yardArea = yardLength * yardWidth
wage = yardArea - houseArea * 2.0
print(wage)
