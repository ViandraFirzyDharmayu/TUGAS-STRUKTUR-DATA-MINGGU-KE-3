def buku_telepon():
    kontak = {}
    
    while True:
        print("\nMenu:")
        print("1. Tambah Kontak")
        print("2. Cari Kontak")
        print("3. Tampilkan Semua")
        print("4. Keluar")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            nama = input("Masukkan nama: ")
            nomor = input("Masukkan nomor: ")
            kontak[nama] = nomor
            print("Kontak ditambahkan.")
        
        elif pilihan == "2":
            nama = input("Masukkan nama yang dicari: ")
            print("Nomor:", kontak.get(nama, "Tidak ditemukan"))
        
        elif pilihan == "3":
            for nama, nomor in kontak.items():
                print(nama, ":", nomor)
        
        elif pilihan == "4":
            break
        
        else:
            print("Pilihan tidak valid.")

# Jalankan
# buku_telepon()