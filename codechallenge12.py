#diamond
for a in range(1, 4):
    for b in range(11, a, -1): 
        print(" ", end='  ')
    for b in range(0, a):
        print("*", end='  ')
    for b in range(1, a):
        print("*", end='  ')
    print()

for a in range(2, 0, -1):
    for b in range(11, a, -1): 
        print(" ", end='  ')
    for b in range(0, a,1):
        print("*", end='  ')
    for b in range(1, a,1):
        print("*", end='  ')
    print()

#first
for c in range(1, 7, 1):
    for d in range(11, c, -1):  
        print(" ", end='  ')
    for d in range(0, c, 1):
        print("*", end='  ')
    for d in range(1, c, 1):
        print("*", end='  ')
    print()

#second 
for e in range(1, 9, 1):
    for f in range(11, e, -1): 
        print(" ", end='  ')
    for g in range(0, e, 1):
        print("*", end='  ')
    for g in range(1, e, 1):
        print("*", end='  ')
    print()

#third
for l in range(1, 12, 1):
    for t in range(11, l, -1): 
        print(" ", end='  ')
    for m in range(0, l, 1):
        print("*", end='  ')
    for m in range(1, l, 1):
        print("*", end='  ')
    print()

#rectangle
for s in range(1,8,1):
    for h in range(1,5,1):
        print(" ", end='  ')
    for h in range(1,6,1):
        print("", end='  ')
    for h in range(1,7,1):
        print("*", end='  ')
    print()