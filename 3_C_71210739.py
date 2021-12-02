# Odilio Ganesha Nugroho - 71210739
# Unguided 12 Grup C Soal 3

def pola(a):
    panjang = len(a)
    print("Output : ")

    for i in range(panjang - 1):
        for j in range(i + 1):
            print(a[j], end="")
        print("\r")

    for i in range(panjang):
        for j in range(panjang - i):
            print(a[j], end="")
        print("\r")


a = str(input("Input : "))
pola(a)
