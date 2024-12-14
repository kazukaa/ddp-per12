from animal import *

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, paruh, ketinggian):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.paruh = paruh
        self.ketinggian = ketinggian 
        
    def cetak_burung(self):
        super().cetak()
        print(f"Paruh \t\t: ", self.paruh,
              "\nKetinggian \t: ", self.ketinggian)
    def terbang(self): 
        print(f"{self.nama} sedang terbang.")
    def makan(self):
        print(f"{self.nama} sedang makan")
        
bersayap = Burung ("Burung Elang", "Ayam", "Darat dan Udara", "Bertelur", "Melengkung", "6000 mdpl")
melayang = Burung ("Burung Gagak", "Biji-Bijian", "Darat dan Udara", "Bertelur", "Hitam Kuat", "Rendah")
bersayap.cetak_burung()
bersayap.terbang()
bersayap.makan()
melayang.cetak_burung()
melayang.terbang()
melayang.makan()