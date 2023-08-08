print("=" * 65)
print("")
print(" SELAMAT DATANG DI APLIKASI TIKET SINAR JAYA AGEN TERMINAL TEGAL")
print("")
print("=" * 65)
print(" " * 18, "Jurusan yang Tersedia", " " * 20)
print("")
print("=" * 54)
print("|  No  |   Tujuan   |     Kelas    |      Harga      |")
print("=" * 54)
print("|  1   |  Karawang  |  Ac Ekonomi  | Rp. 80.000,00   |")
print("|  2   |  Karawang  |  Executive   | Rp. 95.000,00   |")
print("|  3   |  Karawang  | Suites Class | Rp. 140.000,00  |")
print("-" * 54)
print("|  4   |  Cikarang  |  Ac Ekonomi  | Rp. 90.000,00   |")
print("|  5   |  Cikarang  |  Executive   | Rp. 100.000,00  |")
print("|  6   |  Cikarang  | Suites Class | Rp. 175.000,00  |")
print("-" * 54)
print("|  7   |   Bekasi   |  Ac Ekonomi  | Rp. 95.000,00   |")
print("|  8   |   Bekasi   |  Executive   | Rp. 110.000,00  |")
print("|  9   |   Bekasi   | Suites Class | Rp. 190.000,00  |")
print("-" * 54)
print("|  10  |   Jakarta  |  Ac Ekonomi  | Rp. 100.000,00  |")
print("|  11  |   Jakarta  |  Executive   | Rp. 120.000,00  |")
print("|  12  |   Jakarta  | Suites Class | Rp. 210.000,00  |")
print("-" * 54)
print("|  13  |  Tangerang |  Ac Ekonomi  | Rp. 105.000,00  |")
print("|  14  |  Tangerang |  Executive   | Rp. 130.000,00  |")
print("|  15  |  Tangerang | Suites Class | Rp. 225.000,00  |")
print("-" * 54)
print("|  16  |   Banten   |  Ac Ekonomi  | Rp. 110.000,00  |")
print("|  17  |   Banten   |  Executive   | Rp. 140.000,00  |")
print("|  18  |   Banten   | Suites Class | Rp. 240.000,00  |")
print("=" * 54)
print("")

#Input Data
nama        = input("Nama          : ")
print("=" * 63)
print("| KARAWANG | CIKARANG | BEKASI | JAKARTA | TANGERANG | BANTEN |")
print("=" * 63)
tujuan      = input("Tujuan        : ")
asal        = input("Asal          : ")
print("Kode Kelas    : ")
print("=" * 41)
print("| Ac Ekonomi | Executive | Suites Class |")
print("=" * 41)
print("|     AC     |    Exe    |    Suites    |")
print("=" * 41)
kelas       = input("Kelas         : ")
hp          = input("No HP         : ")
print("Jadwal        :")
print("=" * 33)
print("| 07.30 | 13.00 | 16.00 | 19.20 |")
print("=" * 33)
print("|   1   |   2   |   3   |   4   |")
print("=" * 33)
jam         = input("Jam Berangkat : ")
beli        = int(input("Jml Tiket     : "))
petugas     = input("Petugas       : ")

#if else Tujuan
if tujuan == "KARAWANG" or tujuan == "Karawang" or tujuan == "karawang":
    jurusan = "Karawang"
    if kelas == "AC" or kelas == "ac":
        kasta   = "Ac Ekonomi"
        tarif   = 80000
        no_body = "76 J"
    elif kelas == "Exe" or kelas == "exe":
        kasta   = "Executive"
        tarif   = 95000
        no_body = "19 RC"
    elif kelas == "Suites" or kelas == "suites":
        kasta   = "Suites Class"
        tarif   = 140000
        no_body = "22 RE"
    else :
        kasta   = "-"
        tarif   = 0
        no_body = "-"
elif tujuan == "CIKARANG" or tujuan == "Cikarang" or tujuan == "cikarang":
    jurusan = "Cikarang"
    if kelas == "AC" or kelas == "ac":
        kasta   = "Ac Ekonomi"
        tarif   = 90000
        no_body = "12 VX"
    elif kelas == "Exe" or kelas == "exe":
        kasta   = "Executive"
        tarif   = 100000
        no_body = "12 RC"
    elif kelas == "Suites" or kelas == "suites":
        kasta   = "Suites Class"
        tarif   = 175000
        no_body = "23 RE"
    else :
        kasta   = "-"
        tarif   = 0
        no_body = "-"
elif tujuan == "BEKASI" or tujuan == "Bekasi" or tujuan == "bekasi":
    jurusan = "Bekasi"
    if kelas == "AC" or kelas == "ac":
        kasta   = "Ac Ekonomi"
        tarif   = 95000
        no_body = "66 J"
    elif kelas == "Exe" or kelas == "exe":
        kasta   = "Executive"
        tarif   = 110000
        no_body = "82 RD"
    elif kelas == "Suites" or kelas == "suites":
        kasta   = "Suites Class"
        tarif   = 190000
        no_body = "24 RE"
    else :
        kasta   = "-"
        tarif   = 0
        no_body = "-"
elif tujuan == "JAKARTA" or tujuan == "Jakarta" or tujuan == "jakarta":
    jurusan = "Jakarta"
    if kelas == "AC" or kelas == "ac":
        kasta   = "Ac Ekonomi"
        tarif   = 100000
        no_body = "93 RC"
    elif kelas == "Exe" or kelas == "exe":
        kasta   = "Executive"
        tarif   = 120000
        no_body = "31 RE"
    elif kelas == "Suites" or kelas == "suites":
        kasta   = "Suites Class"
        tarif   = 210000
        no_body = "81 RE"
    else :
        kasta   = "-"
        tarif   = 0
        no_body = "-"
elif tujuan == "TANGERANG" or tujuan == "Tangerang" or tujuan == "tangerang":
    jurusan = "Tangerang"
    if kelas == "AC" or kelas == "ac":
        kasta   = "Ac Ekonomi"
        tarif   = 105000
        no_body = "76 RD"
    elif kelas == "Exe" or kelas == "exe":
        kasta   = "Executive"
        tarif   = 130000
        no_body = "34 RE"
    elif kelas == "Suites" or kelas == "suites":
        kasta   = "Suites Class"
        tarif   = 225000
        no_body = "88 RE"
    else :
        kasta   = "-"
        tarif   = 0
        no_body = "-"
elif tujuan == "BANTEN" or tujuan == "Banten" or tujuan == "banten":
    jurusan = "Banten"
    if kelas == "AC" or kelas == "ac":
        kasta   = "Ac Ekonomi"
        tarif   = 110000
        no_body = "88 RC"
    elif kelas == "Exe" or kelas == "exe":
        kasta   = "Executive"
        tarif   = 140000
        no_body = "66 RD"
    elif kelas == "Suites" or kelas == "suites":
        kasta   = "Suites Class"
        tarif   = 240000
        no_body = "37 RE"
    else :
        kasta   = "-"
        tarif   = 0
        no_body = "-"
else :
    print("Jurusan Tidak Ada!")


#if else Jam Keberangkatan
if jam == "1" or jam == "satu" or jam == "Satu" or jam == "SATU":
    jadwal = "07.30"
elif jam == "2" or jam == "dua" or jam == "Dua" or jam == "DUA":
    jadwal = "13.00"
elif jam == "3" or jam == "tiga" or jam == "Tiga" or jam == "TIGA":
    jadwal = "16.00"
elif jam == "4" or jam == "empat" or jam == "Empat" or jam == "EMPAT":
    jadwal = "20.00"
else :
    print("Tidak di Temukan Jadwal")

# Menghitung Total
total = beli * tarif
print("")
print("=" * 20, "Sedang Mencetak Tiket", "=" * 20)
print("")
print("")
print("")
print(" " * 20, "Tiket Sinar Jaya Group", " " * 20)
print("  Kenyamanan Bertransportasi yang Aman, terjangkau, Terpercaya")
print(" " * 9, "Hotline : Fax : 021 8833 6059 SMS : 0812 12847", " " * 9)
print(" ")


print("Nama          : "+str(nama))
print("Tujuan        : "+str(jurusan))
print("Asal          : "+str(asal))
print("Kelas         : "+str(kasta))
print("No HP         : "+str(hp))
print("Jam Berangkat : "+str(jadwal))
print("No Body Bus   : "+str(no_body))
print("Jml Tiket     : "+str(beli),"Tiket")
print("Tarif         : Rp.",total)
print("Petugas       : "+str(petugas))
print(" ")
print(" " * 10, "Pemegang Tiket dianggap telah mengetahui dan", " " * 10)
print(" " * 4, "Wajib memenuhi ketentuan dan Peraturan SINAR JAYA GROUP!", " " * 4)
print("=" * 7, "Mohon Hadir 30 Menit sebelum Jadwal Keberangkatan", "=" * 7)