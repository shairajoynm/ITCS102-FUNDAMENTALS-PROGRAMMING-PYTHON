for a in range (1,9):
    for b in range (9, a,-1):
        print(" ", end="")
    for b in range (2, a,1):
        print(b, end="")
    for c in range (1, a, 1):
        print(c, end="")
    print()