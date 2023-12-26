from Animals import *


class Badak(Animals):
    def __init__(self, nama, makanan, hidup, berkembang_biak, berat_badan):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.berat_badan = berat_badan

    def suara(self):
        return "Badak suaranya 'grrraaaaa'"
    
    def info(self):
        return f"{super().info()}\nBerat Badan: {self.berat_badan}kg"