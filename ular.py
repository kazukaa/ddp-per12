from animal import *
 
class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, corak, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.corak = corak
        self.racun = racun 
        
    def cetak_ular(self):
        super().cetak()
        print(f"corak \t\t: ", self.corak,
              "\nracun \t\t: ", self.racun)
        
    def tidur(self): 
        print(f"{self.nama} sedang tidur.")
    def makan(self):
        print(f"{self.nama} sedang makan.")
        
anaconda = Ular ("Anaconda", "Kambink", "Amazon", "Bertelur", "Eunectes murinus", "Mematikann")
bapaconda = Ular ("King Cobra", "Ular lain", "Hutan Tropis & Subtropis", "Bertelur", "Tanda Chevron (V) di Belanakang Leher", "Mengerikann")
anaconda.cetak_ular()
anaconda.tidur()
anaconda.makan()
bapaconda.cetak_ular()
bapaconda.tidur()
bapaconda.makan()