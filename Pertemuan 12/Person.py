class Orang:

    def __init__(self,fname ,lname ):
        self.fname = fname
        self.lname = lname

    def makan(self):
        print("saya bisa makan")

    def cetak (self):
        print("nama saya", self.fname,self.lname)


class Mahasiswa(Orang):
    def __init__(self, fname, lname, prodi, angkatan):
        super().__init__(fname,lname)
        self.prodi = prodi
        self.angkatan = angkatan 
    
    def cetak (self):
        super().cetak
        print("saya prodi", self.prodi, "angkatan" ,self.angkatan)
        
class Pegawai(Orang):
    def bekerja(self):
        print("saya berkerja")



# objek orang 
x =Orang("bagus" , "maulana")
x.cetak()  
#  x.bekerja()

# objek mahasisiwa
y = Mahasiswa("Dwi", "Astuti", "Teknik Informatika" , 2023)
y.cetak()
y.makan() 

# objek pergawai
agus = Pegawai("Agus", "Rahman")
agus.bekerja()


