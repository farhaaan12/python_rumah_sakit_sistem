print("===================================")
print("PROGRAM PENDAFTARAN PASIEN")
print("===================================")
print("1. Daftar Pasien")
print("2. Taambah Data Pasien")
print("3. Cari Data psien")
print("4. Ubah Data Pasien")
print("5. Hapus Data Paien")
print("6. Keluar")

print("===================================")

# Developed by. Bayu Prasetya
# JCDS - [Class Batch]


# /************************************/

# /===== Data Model =====/
# Create your data model here
pasien_list = [] # Example data model
#function id otomatis pasien
def generate_id():
    if len(pasien_list) == 0:
        return 1
    else:
        return pasien_list[-1]["id"] + 1


# /===== Feature Program =====/
# Create your feature program here
def read():
    def daftar_pasien():

        print("\n=== DAFTAR PASIEN ===")

    if len(pasien_list) == 0:
        print("Data Pasien belum ada.")
        return

    print("-" * 75)

    print(
        f"{'ID':<5}"
        f"{'Nama Pasien':<30}"
        f"{'Umur':<5}"
        f"{'Keluhan':<25}"
        f"{'No HP':<25}"
        f"{'Alamat':<25}"
    )
    for pasien in pasien_list:
    
            print(
                f"{pasien['id_pasien']:<5}"
                f"{pasien['nama']:<30}"
                f"{pasien['umur']:<5}"
                f"{pasien['keluhan']:<25}"
                f"{pasien['no_hp']:<25}"
                f"{pasien['alamat']:<25}"
            )
    
    print("-" * 75)
    return

def input_pasien():
    """Function for create the data
    """
    print("\n=== TAMBAH DATA PASIEN ===")
    nama = input("Masukkan Nama Pasien: ")
    umur = input("Masukkan Umur Pasien: ")
    keluhan = input("Masukkan Keluhan Pasien: ")
    no_hp = input ("Masukkan No HP Pasien: ")
    alamat =  input("Masukkan Alamat Pasien: ")
    id_pasien = generate_id()
    data_pasien = {
        "ID": id_pasien,
        "Nama": nama,
        "Umur" : umur,
        "Keluhan" : keluhan,
        "No HP": no_hp,
        "Alamat": alamat
    }
    pasien_list.append(data_pasien)
    print("\nPasien berhasil ditambahkan!")
    print(f"ID Pasien: {id_pasien}")
    return

def update():
    """Function for update the data
    """
    return

def delete():
    """Function for delete the data
    """
    return

# /===== Main Program =====/
# Create your main program here
def main():
    """Function for main program
    """

    input_user = input("Insert your option: ")
    if input_user == "1":
        daftar_pasien()
    elif input_user == "2":
        input_pasien()
    elif input_user == "3":
        cari_data()
    elif input_user == "4":
        ubah_data()
    elif input_user == "5":
        hapus_data()
    elif input_user ==  6:
        print("\nTerima kasih telah menggunakan program.")
        print("Program selesai.")

    else:

        print("Pilihan tidak tersedia. Silakan pilih 1-6.")

if __name__ == "__main__":
    main()