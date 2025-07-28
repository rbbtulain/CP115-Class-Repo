prinsipal = float(input())
rate = float(input())
time = float(input())
interest = prinsipal * time * rate
totalAmount = prinsipal + interest
monthlyInterest = interest / time * 12
print(interest)
print(totalAmount)
print(monthlyInterest)
