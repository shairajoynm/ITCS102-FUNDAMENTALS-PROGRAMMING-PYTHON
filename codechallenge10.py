for a in range(1, 11, 1):
    for c in range(11, a, -1):
        print(" ", end='  ')
    for b in range(0, a, 1):
        print("*", end='  ')
    for b in range(1, a, 1):
        print("*", end='  ')
    for c in range(11, a, -1):
        print(" ", end='  ')
    print()
