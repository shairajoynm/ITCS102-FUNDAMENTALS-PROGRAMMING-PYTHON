#discount 10% if minor

name = input("Name: ")
age = input("Are you a minor? (Yes/No) ")
fare = float(input("Bayad --> "))

if age.lower() == "yes":
    discount = fare * 0.10
    new_fare = fare - discount
    print("Hi", name, ",your discounted fare is", new_fare)

else:
    print("Sorry", name, ", you are not eligible for a discount. You may now proceed in paying the alloted fare for you")

