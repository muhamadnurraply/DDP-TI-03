def persegi(sisi):
    luas= sisi*sisi
    keliling = 4 * sisi
    print("luas persegi: ", luas)
    print("keliling persegi: ", keliling)

def persegi_panjang(panjang,lebar):
    luas= panjang*lebar
    keliling= 2* (panjang + lebar)
    print("luas persegi panjang: ", luas)
    print("keliling persegi panjang: ", keliling)

def lingkaran(jari2):
    phi = 3.14
    luas = phi * jari2 * jari2
    keliling = 2 * phi * jari2
    print("luas Lingkaran: ", luas)
    print("keliling Lingkaran: ", keliling)

def segitiga_sama_sisi(alas,tinggi):
    luas = 0.5 * alas*tinggi
    keliling = alas * 3
    print("luas segitiga sama sisi: ", luas)
    print("keliling segitiga sama sisi: ", keliling)

def belah_ketupat(diagonal1, diagonal2, sisi):
    luas = 0.5 * diagonal1 * diagonal2
    keliling = 4 * sisi
    print("luas belah ketupat : ", luas)
    print("keliling belah ketupat: ", keliling)

def jajar_genjang (alas, tinggi ,sisimiring):
    luas = alas * tinggi
    keliling = 2 * alas * sisimiring
    print("luas jajar genjang : ", luas)
    print("keliling jajar genjang : ", keliling)
    
def layang_layang(diagonal1 ,diagonal2, sisi_atas, sisi_bawah ):
    luas= diagonal1 * diagonal2 *0.5
    keliling = (sisi_atas * 2) + (sisi_bawah * 2)
    print("luas layan-layang: ", luas)
    print("keliliang layang-layang : " , keliling)
