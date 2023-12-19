class Gempa: 
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    def dampak(self):
        if self.skala < 2:
            return "dampak gempanya tidak terasa"
        elif self.skala >= 2 and self.skala < 4:
            return "dampak gempanya membuat retak-retak"
        elif self.skala >= 4 and self.skala <6:
            return "dampak gemba membuat bangunan roboh"
        elif self.skala >= 6:
            return "dampak gempa membuat bangunan roboh dan berpotnsi tsunami"
        