print ("------------------------------------------------------")
print ("    SELAMAT DATANG PADA APLKASI PENJUALAN BUKU")
print ("                    TOKO X")
print ("------------------------------------------------------")
buku=["PHP Pemula","Pyton Pemula","Mikrotik","Metode"]
p=input("Masukan Pilihan Anda (1.Pembelian)(2.Admin) :")
############# pembelian ####################################
if p=="1":
    print("Selamat Datang Penjualan Buku")
    print("_____________________________")
    print("Masukan Pembelian Anda :")
    #print ("Apakah Anda Mau Melakukan Pembelian?")
    kb = int(input("Kode Buku       :"))
    jb = str(input("Judul Buku      :"))
    h = int(input("Harga Buku       :"))
    jml = int(input("Jumlah Buku    :"))

    Jenis_Buku =str(input("Jenis Buku [P/M/J]01    :"))
    Total= (h*jml)
    print ("------------------------------------------------------")
    print ("Jenis Buku :",Jenis_Buku)
    if (Jenis_Buku =="P"):
        print ("BUKU YANG DI AMBIL ADALAH : PEMOGRAMAN PYTHON")
    elif (Jenis_Buku =="M"):
        print ("BUKU YANG DI AMBIL ADALAH : METODE ILMIAH")
    elif (Jenis_Buku =="J"):
        print ("BUKU YANG DI AMBIL ADALAH : JAVA")
    print ("Total Pembelian :","Rp.",Total)
    print ("------------------------------------------------------")
######################### Admin #################################

elif p=="2":
    print("Selamat Datang Admin")
    print("_____________________")
    p2=input("Masukan Pilihan Anda (1.Menambah)(2.Mengubah)(3.Menghapus) :")
   
    if p2=="1":
        tambah=input("Buku yang ditambah :")
        buku.append(tambah)
        print ("Buku Telah ditambah :",buku)

    elif p2 =="2":
        ubah=input("Buku Yang diubah :")
        buku[1]='Java'
        print("buku telah diubah :",buku)

    elif p2 =="3":
        hapus=input ("Buku yang dihapus :")
        del buku[1]
        print("Buku yang dihapus :",buku)
        
