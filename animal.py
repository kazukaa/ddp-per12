class Animal:
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
    
    def cetak(self):
        print("\nNama \t\t: ", self.nama,
              "\nMakanan \t: ", self.makanan,
              "\nHidup \t\t: ", self.hidup,
              "\nBerkembang Biak\t: ", self.berkembang_biak
              )     
    
hewan = Animal(f"Buaya", "Daging", "Amphibi", "Bertelur")
hewan.cetak()
        