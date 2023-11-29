def duplikasi_buah(buah):
    duplikasi_fruits = [fruits for fruits in buah for _ in range (2)]
    return duplikasi_fruits

buah = ['rambutan', 'jambu', 'mangga', 'pepaya', 'pisang']
buah_duplikasi = duplikasi_buah(buah)
print(buah_duplikasi)