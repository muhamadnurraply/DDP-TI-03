print("""
============================================
Sistem penghitung berat badan Ideal

Pilih jenis kelamin:
1 = Laki-laki
2 = Perempuan
""")

jk = int(input("Masukkan pilihan jenis kelamin: "))
tinggi=int(input("masukkan tinggi badan: "))

#untuk laki-laki
beratL=(tinggi-100)-(tinggi-100)*0,1

#untuk peremuan
beratP=(tinggi-100)-(tinggi-100)*0,15

match jk:
    case 1:
        ideal = (tinggi - 100) - (tinggi - 100) * 0.1
        print("Berat badan ideal laki-laki untuk tinggi ", tinggi, "adalah ", ideal)
    case 2:
        ideal = (tinggi - 100) - (tinggi - 100) * 0.15
        print("Berat badan ideal laki-laki untuk tinggi ", tinggi, "adalah ", ideal)
    case _:
        print("Pilihan anda tidak valid")
    
