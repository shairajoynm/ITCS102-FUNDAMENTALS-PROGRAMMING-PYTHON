#using for loop, ask user to input 5 numbers
#after input, get the summation of all the numbers

num = 0
for x in range(1,6):
    number = eval(input("Enter a number "))
    num += number
    print('the new value of num is', num)
print(num)