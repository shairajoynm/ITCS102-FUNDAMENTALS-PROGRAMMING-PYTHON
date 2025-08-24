name = input("Enter your name : ")
age = int(input("Age : "))
total_bill = 0

if age >= 18:
	print(f"\n\tGood day, {name}, you can now proceed to the next page.")
else:
	print(f"\n\tHi {name}, we're sorry, but minors cannot proceed to the next part.")
	print("\tIn exchange for not proceeding, you have a 10% discount on your bill.")
	total_bill = int(input("\nHow much is your total bill?   "))
	x = total_bill * .1
	y = total_bill - x
	print("Your total bill now is", y)


