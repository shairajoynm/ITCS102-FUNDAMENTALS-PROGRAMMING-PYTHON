#Multiplication table maker

num1 = eval(input("Input any number:   "))
print("\nMultiplication Table for  :", num1)

product = 1
for a in range(1, 11, 1): 
    product = num1 * a
    print(num1, "x", a, "=", product)
