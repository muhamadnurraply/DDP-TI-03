def duplikasikan (daftar_buah):
    hasil = []

    for buah in daftar_buah:
        hasil.append(buah)
        hasil.append(buah)

    return hasil

nama_buah = ['rambutan', 'jambu', 'mangga', 'pepaya', 'pisang']
buah_duplikasi = duplikasikan(nama_buah)
print(buah_duplikasi)