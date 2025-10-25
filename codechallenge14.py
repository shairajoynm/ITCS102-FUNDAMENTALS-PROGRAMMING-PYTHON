sum = 0
concatenate = " "

name = input("Name:  ")

print(f"\nHi {name}! Welcome to EVEN number detector!\n")
print("Just enter any number you want to detect, enter 0 if you want to exit")

while True:
    number = eval(input("Enter any number: "))

    if number == 0:
        print("\nBye...\n")
        print(f"EVEN numbers you entered: {concatenate}")
        print(f"Sum of all numbers detected: {sum}")
        break

    if number % 2 == 0:
        print("EVEN number detected")
        concatenate += str(number)
        sum += number
    else:
        print("Skipping...")
