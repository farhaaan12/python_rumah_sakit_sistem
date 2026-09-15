print("===================================")
print("PROGRAM PENDAFTARAN PASIEN")
print("===================================")

# Developed by. Bayu Prasetya
# JCDS - [Class Batch]

# /===== Data Model =====/
pasien_list = [] 

# Function ID otomatis pasien
def generate_id():
    if len(pasien_list) == 0:
        return 1
    else:
        # Menggunakan key 'id_pasien' agar konsisten
        return pasien_list[-1]["id_pasien"] + 1


# /===== Feature Program =====/
def read():
    print("\n=== DAFTAR PASIEN ===")
    
    if len(pasien_list) == 0:
        print("Data Pasien belum ada.")
        return

    print("-" * 115)
    print(
        f"{'ID':<5}"
        f"{'Nama Pasien':<30}"
        f"{'Umur':<5}"
        f"{'Keluhan':<25}"
        f"{'No HP':<25}"
        f"{'Alamat':<25}"
    )
    print("-" * 115)
    
    for pasien in pasien_list:
        print(
            f"{pasien['id_pasien']:<5}"
            f"{pasien['nama']:<30}"
            f"{pasien['umur']:<5}"
            f"{pasien['keluhan']:<25}"
            f"{pasien['no_hp']:<25}"
            f"{pasien['alamat']:<25}"
        )
    
    print("-" * 115)

def input_pasien():
    print("\n=== TAMBAH DATA PASIEN ===")
    nama = input("Masukkan Nama Pasien: ")
    umur = input("Masukkan Umur Pasien: ")
    keluhan = input("Masukkan Keluhan Pasien: ")
    no_hp = input("Masukkan No HP Pasien: ")
    alamat = input("Masukkan Alamat Pasien: ")
    id_pasien = generate_id()
    
    # PERBAIKAN: Key diubah menjadi huruf kecil semua agar sesuai dengan fungsi read()
    data_pasien = {
        "id_pasien": id_pasien,
        "nama": nama,
        "umur" : umur,
        "keluhan" : keluhan,
        "no_hp": no_hp,
        "alamat": alamat
    }
    pasien_list.append(data_pasien)
    print("\nPasien berhasil ditambahkan!")
    print(f"ID Pasien: {id_pasien}")

def cari_data():
    print("\n=== CARI DATA PASIEN ===")
    # Tambahkan logika cari di sini nanti
    pass

def ubah_data():
    print("\n=== UBAH DATA PASIEN ===")
    pass

def hapus_data():
    print("\n=== HAPUS DATA PASIEN ===")
    pass


# /===== Main Program =====/
# PERBAIKAN: Menyatukan cetak menu dan input_user ke dalam satu loop 'while True'
while True:
    print("\n===================================")
    print("1. Daftar Pasien")
    print("2. Tambah Data Pasien")
    print("3. Cari Data Pasien")
    print("4. Ubah Data Pasien")
    print("5. Hapus Data Pasien")
    print("6. Keluar")
    print("===================================")
    
    input_user = input("Insert your option: ")
    
    if input_user == "1":
        read()  # Memanggil fungsi read() untuk melihat daftar pasien
    elif input_user == "2":
        input_pasien()
    elif input_user == "3":
        cari_data()
    elif input_user == "4":
        ubah_data()
    elif input_user == "5":
        hapus_data()
    elif input_user == "6":  # Menggunakan string "6" karena input() menghasilkan teks
        print("\nTerima kasih telah menggunakan program.")
        print("Program selesai.")
        break  # Menghentikan loop secara total dan keluar dari program
    else:
        print("\nPilihan tidak tersedia. Silakan pilih 1-6.")
