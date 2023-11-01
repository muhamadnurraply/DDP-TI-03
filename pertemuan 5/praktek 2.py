



def luas_bangun_datar(pilih, nilai):
    match pilih:
        case 1: # luas persegi
            return nilai * nilai
        case 2: # luas lingkaran
            return 3.14 * nilai * nilai
        case 3: # luas segitiga
            return (nilai * nilai) / 2
        case _:
            return "Salah pilih angka"

# Program utama
while True:
    print("\nMenghitung Luas Bangun Datar")
    print("1. menghitung Luas Persegi")
    print("2. menghitung Luas Lingkaran")
    print("3. menghitung Luas Segitiga")
    print("0. Keluar")
    
    pilih = int(input("Pilih angka (1/2/3/0): "))

    if pilih == 0:
        break
    nilai = float(input("Masukkan nilai: "))
    luas = luas_bangun_datar(pilih, nilai)
    if pilih == 0:
        print("Anda telah keluar")
    else:
        print(f"Luas bangun datar dengan pilihan {pilih} adalah: {luas}")

    