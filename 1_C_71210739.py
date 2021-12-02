# Odilio Ganesha Nugroho - 71210739
# Unguided 12 Grup C Soal 1

a = int(input("Masukan awal deret: "))
b = int(input("Masukan akhir deret: "))

if (a + 1) % 2 == 0:
    for i in range(a + 1, b, 2):
        if i % 9 == 0 or i % 11 == 0: continue
        print(i, end=" ")
else:
    for i in range(a, b, 2):
        if i % 9 == 0 or i % 11 == 0: continue
        print(i, end=" ")
