from animal import *

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, ciri, ukuran):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.ciri = ciri
        self.ukuran = ukuran 
        
    def cetak_ikan(self):
        super().cetak()
        print(f"Cirinya s\t: ", self.ciri,
              "\nUkurannya \t: ", self.ukuran)
        
    def berenang(self): 
        print(f"{self.nama} sedang berenang.")
    def makan(self):
        print(f"{self.nama} sedang makan.")
        
sirip = Ikan ("Ikan Lele", "Pelet (opsional)", "Air Tawar", "Bertelur", "Ada Kumisnya", "20-40 cm")
sisik = Ikan ("Ikan Hiu", "Ikan Kecil", "Air Asin", "Vivivar, Ovovivivar, Ovivar", "Sirip Punggung yang Unik", "1-12 m")
sirip.cetak_ikan()
sirip.berenang()
sirip.makan()
sisik.cetak_ikan()
sisik.berenang()
sisik.makan()