daftar_buah = ['rambutan', 'jambu', 'mangga', 'pepaya', 'pisang']

#untuk mengeluarkan yg ada di atas tetapi di kurang dengan urutan -4 dan -1
#jika urutan 1-4 maka dari urutan pertaman dan apabila -1sampai-4 maka dari belakang

#print(daftar_buah[-4:-1])


#menghitungberapa banyak item di dalem list atau dictionery dengan menggunkan "len"
print(len(daftar_buah))

#cek keberadaan nilai
if "jambu" in daftar_buah:
    print("Terdapat Jambu")
else:
    print("ga ada jambu")

#Looping list
for Fruits in daftar_buah:
    print(Fruits)