name = input("Name : ")



print("\tHello! Good Day Mr./Ms./Mrs.", name)

x = eval(input("\nEnter the amount of deposit: "))


onek = x // 1000
x = x % 1000
fivehundred = x // 500
x = x % 500
twohundred = x // 200
x = x % 200
onehundred = x // 100
x = x % 100
fifty = x // 50
x = x % 50
tens = x // 10
x = x % 10


print(onek, "- 1000  in the account")
print(fivehundred, "- 500 in the account")
print(twohundred,"- 200 in the account")
print(onehundred, "- 100 in the account")
print(fifty, "- 50 in the account")
print(tens, "- 10 in the account")
print("and", x, "pesos")
