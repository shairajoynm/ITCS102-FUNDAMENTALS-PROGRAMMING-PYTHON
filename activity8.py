#First, compare 2 equations
print("The answer for 3*4 is larger than the answer for 5*2 (True/False)")

a = 3 * 4
b = 5 * 6

print(a > b)


#Next, ask if your payment is exact to your debt
print("\n\nI will pay my debt. Will the payment be exact for the amount of the debt?")

debtplusinterest = 1000

payment = int(input("How much will you pay?   "))

print("Its", debtplusinterest == payment, "that your payment is exact to the amount of your debt")
