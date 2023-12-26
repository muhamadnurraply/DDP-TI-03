
class Animals:
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama 
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
        
    def info(self):
        return f"Nama: {self.nama}\n Makanan: {self.makanan}\n Hidup: {self.hidup}\n Berkembang Biak: {self.berkembang_biak}"

