# Odilio Ganesha Nugroho - 71210739
# Unguided 12 Grup C Soal 4

n = int(input("Input : "))

for x in range(n):
    for y in range(n):
        if y == 0 or x == (n - 1) or x == y:
            print("*", end=" ")
        else:
            print(end="  ")
    print()
