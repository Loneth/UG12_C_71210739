# Odilio Ganesha Nugroho - 71210739
# Unguided 12 Grup C Soal 4

a = int(input("Input : "))

for x in range(a):
    for y in range(a):
        if y == 0 or x == (a - 1) or x == y:
            print("*", end=" ")
        else:
            print(end="  ")
    print()
