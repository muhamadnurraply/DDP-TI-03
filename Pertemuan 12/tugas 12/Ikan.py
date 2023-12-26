from Animals import *

class Ikan(Animals):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, ukuran):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.ukuran = ukuran
    
    def berenang(self):
        return "Ikan sedang berenang di air"
    
    def info(self):
        return f"{super().info()}\nJenis: {self.jenis}\nUkuran: {self.ukuran} cm"