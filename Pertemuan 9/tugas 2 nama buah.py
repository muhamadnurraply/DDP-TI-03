daftar_buah = ['rambutan', 'jambu', 'mangga', 'pepaya', 'pisang']
def balikan(daftar_buah):
    buahbuahan_balik = []
    for i in range(int(len(daftar_buah))-1,-1,-1):
        buahbuahan_balik.append(daftar_buah[i])
    return buahbuahan_balik 
buahbuahan_balik = balikan(daftar_buah)
print(buahbuahan_balik)