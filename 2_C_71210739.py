# Odilio Ganesha Nugroho - 71210739
# Unguided 12 Grup C Soal 2

mapel = [
    # 0 - Selasa
    ["2 Matematika Teknik", "4 Bhs Indonesia", "6 PKN"],

    # 1 - Rabu
    ["1 Riset Operasi", "3 Sistem Operasi", "5 Praktikum INLAN"],

    # 2 - Kamis
    ["1 IMK", "3 LogMat", "4 Praktekkom"],

    # 3 - Jumat
    ["2 Sistem Bisnis Data", "4 Praktikum Sistem Basisata", "6 INLAN"]
]

a = str(input("Hi Momo, Silahkan Masukkan hari yang ingin Anda telusuri: ")).lower()

if a == "senin":
    print("Hari", a, "Anda tidak ada kelas")
elif a == "selasa":
    for x in mapel[0]:
        print ("kelas ke-{}".format(x))
elif a == "rabu":
    for x in mapel[1]:
        print("kelas ke-{}".format(x))
elif a == "kamis":
    for x in mapel[2]:
        print("kelas ke-{}".format(x))
elif a == "jumat":
    for x in mapel[3]:
        print("kelas ke-{}".format(x))
