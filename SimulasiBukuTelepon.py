def buku_telepon():
    kontak = {}

    while True:
        print("\n=== MENU BUKU TELEPON ===")
        print("1. Tambah Kontak")
        print("2. Cari Kontak")
        print("3. Hapus Kontak")
        print("4. Tampilkan Semua Kontak")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            nama = input("Masukkan nama: ")
            nomor = input("Masukkan nomor: ")
            
            if nama in kontak:
                print("⚠️ Kontak sudah ada, akan diperbarui.")
            
            kontak[nama] = nomor
            print("✅ Kontak berhasil disimpan.")

        elif pilihan == "2":
            nama = input("Masukkan nama yang dicari: ")
            
            if nama in kontak:
                print(f"📞 Nomor {nama}: {kontak[nama]}")
            else:
                print("❌ Kontak tidak ditemukan.")

        elif pilihan == "3":
            nama = input("Masukkan nama yang akan dihapus: ")
            
            if nama in kontak:
                del kontak[nama]
                print("🗑️ Kontak berhasil dihapus.")
            else:
                print("❌ Kontak tidak ditemukan.")

        elif pilihan == "4":
            if not kontak:
                print("📂 Buku telepon kosong.")
            else:
                print("\n=== DAFTAR KONTAK ===")
                for nama, nomor in kontak.items():
                    print(f"{nama} : {nomor}")

        elif pilihan == "5":
            print("👋 Keluar dari program.")
            break

        else:
            print("⚠️ Pilihan tidak valid.")

# Jalankan program
buku_telepon()