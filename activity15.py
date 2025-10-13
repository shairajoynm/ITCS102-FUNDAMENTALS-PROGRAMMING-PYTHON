#STRING FORMATTING
#Name, Age

name = 'Shaira Joy'
age = '18'
print (f"Ako si {name} at ako ay {age} na taong gulang")

#input 5 numbers, get the summation of all the PRIME NUMBERS

prime_sum = 0

for a in range(1,6,1):
    num1 = eval(input(f"{a} - Enter a number --> "))

    if num1 % 2 == 1:
        prime_sum += num 

print(f"The sum of all the PRIME numbers given is {prime_sum}")

