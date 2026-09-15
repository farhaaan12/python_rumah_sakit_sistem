print("===================================")
print("PROGRAM PENDAFTARAN PASIEN")
print("===================================")

# /===== Data Model =====/
pasien_list = [ 
    {"id_pasien": 1, "nama": "Andi", "umur": 25, "keluhan": "Batuk", "no_hp" : "081234567890", "alamat" : "Tangerang"},
    {"id_pasien": 2, "nama": "Budi", "umur": 40, "keluhan": "Flu", "no_hp" : "08234567892", "alamat" : "Jakarta"},
    {"id_pasien": 3, "nama": "Arif", "umur": 30, "keluhan": "Batuk", "no_hp" : "08127894563", "alamat" : "Tangerang"},
    {"id_pasien": 4, "nama": "Rifki", "umur": 52, "keluhan": "Demam", "no_hp" : "08571234567", "alamat" : "Tangerang Selatan"},
    {"id_pasien": 5, "nama": "Nanda", "umur": 45, "keluhan": "Mual", "no_hp" : "08192345678", "alamat" : "Tangerang"},
]

# Function ID otomatis pasien
def generate_id():
    if not pasien_list:
        return 1
    pasien_terakhir = pasien_list[-1]
    return pasien_terakhir["id_pasien"] + 1

# Function validasi nilai input tidak boleh kosong
def input_validasi(validasi):
    while True:
        nilai = input(validasi).strip()
        if nilai:
            return nilai
        print("Input tidak boleh kosong! Silakan isi data.")

# Function pencarian cari, ubah, hapus 
def filter_search(pesan="=== CARI PASIEN ==="):
    while True:
        print(f"\n{pesan}")
        filter_data = input("Masukkan ID atau Nama pasien (ketik '0' untuk batal): ").strip()
        
        # Validasi input kosong
        if not filter_data:
            print("Input tidak boleh kosong.")
            continue
            
        # Opsi keluar/batal, kembali ke menu utama
        if filter_data == "0":
            print("Pencarian dibatalkan.")
            return None
            
        kandidat_pasien = []
        
        # Proses Filter Data ID
        if filter_data.isdigit():
            id_cari = int(filter_data)
            for pasien in pasien_list:
                if pasien["id_pasien"] == id_cari:
                    kandidat_pasien.append(pasien)
                    break
        else:
            #Proses Filter Data Mama
            nama_cari = filter_data.lower()
            for pasien in pasien_list:
                if nama_cari in pasien["nama"].lower():
                    kandidat_pasien.append(pasien)

        # input ulang jika data tidak ditemukan
        if not kandidat_pasien:
            print(f"\nData pasien '{filter_data}' tidak ditemukan.")
            coba_lagi = input("Ingin mencoba cari lagi? (y/n): ").lower().strip()
            if coba_lagi == 'y':
                continue  # Mengulang input pencarian
            else:
                return None  # Kembali ke Menu Utama

        # Jika Ditemukan 1 data pasien (Nama Mirip)
        if len(kandidat_pasien) > 1:
            print(f"\nDitemukan {len(kandidat_pasien)} pasien dengan nama mirip '{filter_data}':")
            print("-" * 80)
            print(f"{'ID':<5} | {'Nama Pasien':<15} | {'Umur':<5} | {'Keluhan':<12} | {'No HP':<15} | {'Alamat':<15}")
            print("-" * 80)
            for p in kandidat_pasien: # Menampilkan data yang nilai sama
                print(f"{p['id_pasien']:<5} | {p['nama']:<15} | {p['umur']:<5} | {p['keluhan']:<12} | {p['no_hp']:<15} | {p['alamat']:<15}")
            print("-" * 80)
            
            while True:
                try:
                    id_spesifik = int(input("\nMasukkan ID Pasien yang tepat dari daftar di atas (ketik '0' untuk batal): "))
                    if id_spesifik == 0:
                        return None
                    for p in kandidat_pasien:
                        if p["id_pasien"] == id_spesifik:
                            return p
                    print("ID yang Anda masukkan tidak ada dalam daftar di atas.")
                except ValueError:
                    print("Input tidak valid! Harap masukkan angka ID.")

    
        # Jika Hanya Ditemukan 1 Pasien
        return kandidat_pasien[0]

# View data pasien
def daftar_pasien():
    print("\n=== DAFTAR PASIEN ===")
    if len(pasien_list) == 0:
        print("Data Pasien belum ada.")
        return

    print("-" * 95)
    print(
        f"{'ID':<5}"
        f"{'Nama Pasien':<20}"
        f"{'Umur':<8}"
        f"{'Keluhan':<20}"
        f"{'No HP':<20}"
        f"{'Alamat':<20}"
    )
    print("-" * 95)
    for pasien in pasien_list:
        print(
            f"{pasien['id_pasien']:<5}"
            f"{pasien['nama']:<20}"
            f"{pasien['umur']:<8}"
            f"{pasien['keluhan']:<20}"
            f"{pasien['no_hp']:<20}"
            f"{pasien['alamat']:<20}"
        )
    print("-" * 95)
    return

# Input data
def input_pasien():
    print("\n=== TAMBAH DATA PASIEN ===")
    nama = input_validasi("Masukkan Nama Pasien      : ")
    
    while True:
        try:
            umur = int(input("Masukkan Umur Pasien      : "))
            if umur <= 0:
                print("Data tidak valid! Umur harus diatas 0.")
                print("Silakan coba lagi.\n")
                continue
            break
        except ValueError:
            print("Data tidak valid! Harap masukkan data berupa angka saja.\n")
            
    keluhan = input_validasi("Masukkan Keluhan Pasien   : ")
    no_hp = input_validasi("Masukkan No HP Pasien     : ")
    alamat = input_validasi("Masukkan Alamat Pasien    : ")

    konfirmasi = input("\nApakah Anda yakin ingin menyimpan data pasien ini? (y/n): ").lower()
    if konfirmasi == "y":
        #Eksekusi kode
        id_pasien = generate_id()
        data_pasien = {
            "id_pasien": id_pasien,
            "nama": nama,
            "umur" : umur,
            "keluhan" : keluhan,
            "no_hp": no_hp,
            "alamat": alamat
        }
        pasien_list.append(data_pasien)
        print(f"\nPasien berhasil ditambahkan dengan ID: {id_pasien}!")
    else:
        print("\nPenambahan data pasien dibatalkan.")
    return

# Function cari pasien
def cari_pasien():
    pasien_ditemukan = filter_search("=== CARI PASIEN ===")
    if not pasien_ditemukan:
        return
        
    print("\nData Pasien:")
    print("-" * 50)
    print(
        f"ID            : {pasien_ditemukan['id_pasien']}\n"
        f"Nama Pasien   : {pasien_ditemukan['nama']}\n"
        f"Umur          : {pasien_ditemukan['umur']}\n"
        f"Keluhan       : {pasien_ditemukan['keluhan']}\n"
        f"No HP         : {pasien_ditemukan['no_hp']}\n"
        f"Alamat        : {pasien_ditemukan['alamat']}"
    )
    print("-" * 50)
    return

def update_pasien():
    pasien_ditemukan = filter_search("=== UBAH DATA PASIEN ===")
    if not pasien_ditemukan:
        return

    print("\n--- Data Pasien Saat Ini ---")
    print(f"Nama    : {pasien_ditemukan['nama']}")
    print(f"Umur    : {pasien_ditemukan['umur']}")
    print(f"Keluhan : {pasien_ditemukan['keluhan']}")
    print(f"No HP   : {pasien_ditemukan['no_hp']}")
    print(f"Alamat  : {pasien_ditemukan['alamat']}")

    print("\n--- Masukkan Data Baru ---")
    nama_baru = input_validasi("Masukkan nama: ")
    
    while True:
        try:
            umur_baru = int(input("Masukkan umur: "))
            if umur_baru <= 0:
                print("Umur harus di atas 0.")
                continue
            break
        except ValueError:
            print("Input tidak valid! Umur harus berupa angka.")

    keluhan_baru = input_validasi("Keluhan : ")
    no_hp_baru = input_validasi("No HP   : ")
    alamat_baru = input_validasi("Alamat  : ")

    konfirmasi = input("\nApakah Anda yakin ingin mengubah data ini? (y/n): ").lower()

    if konfirmasi == "y":
        pasien_ditemukan["nama"] = nama_baru
        pasien_ditemukan["umur"] = umur_baru
        pasien_ditemukan["keluhan"] = keluhan_baru
        pasien_ditemukan["no_hp"] = no_hp_baru
        pasien_ditemukan["alamat"] = alamat_baru
        print("\nData pasien berhasil diperbarui!")
    else:
        print("\nPerubahan dibatalkan.")
    return

def delete():
    pasien_ditemukan = filter_search("=== HAPUS DATA PASIEN ===")
    if not pasien_ditemukan:
        return    
        
    print("\n--- Data Pasien Saat Ini ---")
    print(f"Nama    : {pasien_ditemukan['nama']}")
    print(f"Umur    : {pasien_ditemukan['umur']}")
    print(f"Keluhan : {pasien_ditemukan['keluhan']}")
    print(f"No HP   : {pasien_ditemukan['no_hp']}")
    print(f"Alamat  : {pasien_ditemukan['alamat']}")

    konfirmasi = input("\nApakah kamu yakin ingin menghapus pasien ini? (y/n): ").lower()
    if konfirmasi == "y":
        pasien_list.remove(pasien_ditemukan)
        print("Pasien berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")
    return

# /===== Main Program =====/
def main():
    while True:
        print("\n===================================")
        print("1. Daftar Pasien")
        print("2. Tambah Data Pasien")
        print("3. Cari Data Pasien")
        print("4. Ubah Data Pasien")
        print("5. Hapus Data Pasien")
        print("6. Keluar")
        print("===================================")

        input_user = input("Insert your option: ").strip()
        if input_user == "1":
            daftar_pasien()
        elif input_user == "2":
            input_pasien()
        elif input_user == "3":
            cari_pasien()
        elif input_user == "4":
            update_pasien()
        elif input_user == "5":
            delete()
        elif input_user == "6":
            print("\nTerima kasih telah menggunakan program.")
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak tersedia. Silakan pilih 1-6.")

if __name__ == "__main__":
    main()