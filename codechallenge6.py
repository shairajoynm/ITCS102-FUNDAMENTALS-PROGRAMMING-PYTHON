
#factorial

x = eval(input("a number: "))
ans = 1

for i in range(x, 0, -1):
    print(i)
    ans *= i

print(x, "!", "=", ans)