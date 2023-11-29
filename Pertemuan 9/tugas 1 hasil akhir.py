
def lulus_saja(data):
    lulus= []
    for mahasiswa in data:
        if mahasiswa ['nilai'] > 65:
            lulus.append(mahasiswa['nama'])
    return lulus

hasil_akhir = [
{'nama':'Raply', 'nilai':70}, 
{'nama':'Iril', 'nilai':63}, 
{'nama':'Rahma', 'nilai':80}, 
{'nama':'edu', 'nilai':40} 
]

print(lulus_saja(hasil_akhir))


