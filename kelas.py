dataMhs = {}
def Jdl_Tbl () :
    print("=========================================================================")
    print("| No |     NIM     |       NAMA        |  TUGAS  |  UTS | UAS |  AKHIR  |")
    print("=========================================================================")
class Mahasiswa :
    def __init__(self):
        self.nama = ""
        self.nim = ""
        self.tugas = 0
        self.uts = 0
        self.uas = 0
        self.akhir = 0
    def simpan(self,nim,nama,tugas,uts,uas):
        self.nama = nama
        self.nim = nim
        self.tugas = tugas
        self.uts = uts
        self.uas = uas
        self.akhir = ((int(tugas) / 100*30) + (int(uts)/100*35) + (int(uas) / 100*35))
        dataMhs[self.nim] = {"nama": nama, "tugas": tugas,"uts": uts, "uas": uas, "akhir": self.akhir}
        print("Data Berhasil tersimpan")
    def tampilkan(self):
        print("Daftar Nilai")
        Jdl_Tbl ()
        if len(dataMhs) == 0:
            print(
                "|                         TIDAK ADA DATA                                |")
        else:
            x = 1
            for i, j in dataMhs.items():
                print('| {0:^3}| {1:11} | {2:<17} | {3:7} | {4:4} | {5:3} | {6:7.2f} |'.format(x, i, dataMhs[i]["nama"], dataMhs[i]["tugas"], dataMhs[i]["uts"], dataMhs[i]["uas"], dataMhs[i]["akhir"]))
                x += 1
        print("=========================================================================")
    def Ubah(self,nama):
        found = 0
        for i, j in dataMhs.items():
            if ((dataMhs.get(i)).get('nama') == self.nama):
                found = i 
        if (found ==0):
            print("Data tidak ada")
        else :
            Mhs.CariNama(nama)
            nama = input("Masukan Nama         : ")
            if nama == "":
                nama = dataMhs[nim]['nama']
            tugas = input("Masukan Nilai Tugas  : ")
            if tugas == "":
                tugas = dataMhs[nim]['tugas']
            uts = input("Masukan Nilai UTS    : ")
            if uts == "":
                uts = dataMhs[nim]['uts']
            uas = input("Masukan Nilai UAS    : ")
            if uas == "":
                uas = dataMhs[nim]['uas']
            akhir = ((int(tugas) / 100*30) +
                     (int(uts)/100*35) + (int(uas) / 100*35))
            dataMhs[found] = {"nama": nama, "tugas": tugas,
                            "uts": uts, "uas": uas, "akhir": akhir}
            print("Berhasil Mengubah Data")
    def CariNama(self,nama):
        x,found = 0,0
        Jdl_Tbl()
        for i, j in dataMhs.items():
            x+=1
            
            if ((dataMhs.get(i)).get('nama').startswith(nama)):
                found += 1
                print('| {0:^3}| {1:11} | {2:<17} | {3:7} | {4:4} | {5:3} | {6:6.2f} |'.format(
                    1, i, dataMhs[i]["nama"], dataMhs[i]["tugas"], dataMhs[i]["uts"], dataMhs[i]["uas"], dataMhs[i]["akhir"]))
        if (found ==0):
            print("Data tidak ada")
        print("=========================================================================")
    def Hapus(self,nama):
        found = 0
        for i, j in dataMhs.items():
           if ((dataMhs.get(i)).get('nama') == nama):
               found = i 
        if (found ==0):
           print("Data tidak ada")
        else :
           dataMhs.pop(i)
           print("Berhasil menghapus mahasiswa yang bernama "+nama)

Mhs = Mahasiswa()
while True :
    menu = input("(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar : ")
    if menu == "T" :
        nim = input("Masukan NIM : ")
        nama = input("Masukan Nama : ")
        tugas = input("Masukan Nilai Tugas : ")
        uts = input("Masukan Nilai UTS : ")
        uas = input("Masukan Nilai UAS : ")
        Mhs.simpan(nim,nama,tugas,uts,uas)
    if menu == "L" :
        Mhs.tampilkan()
    if menu == "U" :
        nama = input("Ubah Data nilai berdasarkan Nama : ")
        Mhs.Ubah(nama)
    if menu == "C" :
        nama = input("Cari Data nilai berdasarkan Nama : ")
        Mhs.CariNama(nama)
    if menu == "H":
        nama = input ("Hapus Data mahasiswa yang bernama : ")
        Mhs.Hapus(nama)
    if menu == "K" :
        break