data_diri = {"nama" : "Yantooo" , "mapel":"DDP"}

#mengakses Dictionary
print(data_diri["nama"])

#menambah data

data_diri["jurusan"] = "Tekinik Informatika"
print(data_diri)

#mengupdate Item 
data_diri["nama"] = "Muhamad Nur Raply"
print(data_diri)

#menghapus Item
data_diri.pop("mapel")
print(data_diri)
#Remove tidak bisa di pakai untuk dictionery

#cek keberaaan key
if "nama" in data_diri:
    print("Terdapat Nama")
else:
    print("Tidak ada nama")
