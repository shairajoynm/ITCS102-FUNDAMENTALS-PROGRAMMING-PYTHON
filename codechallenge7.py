#summation of odd

print("\tAddition of odd numbers here")

odd = 0
for i in range(10):
    x = eval(input("Enter any number: "))
    if x % 2:
        if  x != odd:
            odd += x
    else:
        print("\tEven numbers are not included")

print("\tThe summation of all odd numbers entered is", odd)
