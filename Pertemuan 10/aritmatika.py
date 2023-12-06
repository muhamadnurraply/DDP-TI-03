def penjumlahan(angka1,angka2):
    hasil = angka1+angka2
    print("hasil penjumlahan:" , hasil)

def pengurangan(angka1,angka2):
    hasil = angka1-angka2
    print("hasil pengurangan:" , hasil)

def perkalian(angka1,angka2):
    hasil = angka1*angka2
    print("hasil perkalian:" , hasil)

def pembagian(angka1,angka2):
    hasil = angka1/angka2
    print("hasil pembagian:" , hasil)

def pangkat(angka):
    hasil = angka**0.5
    print("hasil pangkat:" , hasil)

def akar(angka1,angka2):
    hasil = angka1**angka2
    print("hasil akar:" , hasil)

def modulus(angka1,angka2):
    hasil = angka1%angka2
    print("hasil modulud:" , hasil)

def kuadrat(angka):
    hasil = angka** 2
    print("hasil kuadrat:" ,hasil)

def akar_bulan(angka):
    hasil = round(angka**0.5)
    print("hasil akar bulat:" , hasil)

def faktorial(angka):
    hasil = 1
    for i in range(1, angka + 1):
        hasil *= i
    print("hasil faktorial:" , hasil)
    