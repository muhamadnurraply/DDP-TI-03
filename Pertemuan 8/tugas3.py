nilai =int(input("masukan nilai: "))
def ganjil(nilai):
    for i in range (nilai + 1):
        if i % 2 != 0:
            print("angka nilai ganjil: ", i)
print(ganjil(nilai))