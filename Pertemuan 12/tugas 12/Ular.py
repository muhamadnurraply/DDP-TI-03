from Animals import *


class Ular(Animals):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, ukuran):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self. ukuran = ukuran

    def bersarang(self):
        return "ular bersarang di hutan'"
    
    def info(self):
        return f"{super().info()}\nJenis{self.jenis} \nukuran: {self.ukuran} meter"