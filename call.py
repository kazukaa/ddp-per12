print("\n---Mencetak Animal---")
from animal import *
def cetak(self):
        print("\nNama \t\t: ", self.nama,
              "\nMakanan \t: ", self.makanan,
              "\nHidup \t\t: ", self.hidup,
              "\nBerkembang Biak\t: ", self.berkembang_biak
              ) 
        

print("\n---Mencetak Burung---")        
from burung import *
def cetak_burung(self):
        super().cetak()
        print(f"paruh \t\t: ", self.paruh,
              "\njenis \t\t: ", self.ketinggian)
        

print("\n---Mencetak Ikan---")        
from ikan import *
def cetak_ikan(self):
        super().cetak()
        print(f"jenis \t\t: ", self.ciri,
              "\nwarna \t\t: ", self.ukuran)
      
        
print("\n---Mencetak Ular---")
from ular import *
def cetak_ular(self):
        super().cetak()
        print(f"corak \t\t: ", self.corak,
              "\nracun \t\t: ", self.racun)
      
        
print("\n---Mencetak Kucing---")
from kucing import *
def cetak_ular(self):
        super().cetak()
        print(f"corak \t\t: ", self.warna,
              "\nracun \t\t: ", self.kategori)