from animal import *

class Kucing(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, kategori):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.kategori = kategori 
        
    def cetak_kucing(self):
        super().cetak()
        print(f"Warna \t\t: ", self.warna,
              "\nKategori \t: ", self.kategori)
    def main(self): 
        print(f"{self.nama} sedang bermain.")
    def makan(self):
        print(f"{self.nama} sedang makan")
        
berbulu = Kucing ("Kucing Anggora", "Wiskas", "Darat", "Melahirkan", "Putih", "Rumahan")
meow = Kucing ("Kucing Domestik", "Tulang", "Darat", "Melahirkan", "Oyen", "Liar")
berbulu.cetak_kucing()
berbulu.main()
berbulu.makan()
meow.cetak_kucing()
meow.main()
meow.makan()