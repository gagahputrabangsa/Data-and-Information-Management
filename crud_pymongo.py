import pymongo


client = pymongo.MongoClient("mongodb://localhost:0000/")
db = client["ur_database"]
collection = db["ur_collection"]

def tambah_data():
    nama = input("Masukkan nama produk: ")
    harga = int(input("Harga: "))
    negara = input("Dari Negara Mana: ")
    data = {"nama": nama, "harga": harga, "negara":negara}
    result = collection.insert_one(data)
    print("Data berhasil ditambahkan dengan ID:", result.inserted_id)

def cari_data():
    nama = input("Masukkan produk yang dicari: ")
    result = collection.find_one({"nama": nama})
    if result:
        print("\nData ditemukan:")
        print("Nama:", result['nama'])
        print("Harga:", result['harga'])
        print("Negara:", result['negara'])
    else:
        print("Data tidak ditemukan.")
def update_data():
    nama = input("Masukkan produk yang ingin diupdate: ")
    result = collection.find_one({"nama": nama})
    if result:
        print("\nData ditemukan:")
        print("Nama:", result['nama'])
        print("Harga:", result['harga'])
        print("Negara:", result['negara'])

        pilihan = input("Apakah Anda ingin mengupdate: \n(1) Nama\n(2) Harga\n(3) Negara\nPilih (1/2/3): ")
        
        if pilihan == '1':
            new_nama = input("Masukkan nama baru: ")
            collection.update_one({"nama": nama}, {"$set": {"nama": new_nama}})
            print("Nama berhasil diupdate.")
        elif pilihan == '2':
            new_harga = input("Masukkan Harga baru: ")
            collection.update_one({"nama": nama}, {"$set": {"harga": new_harga}})
            print("Harga berhasil diupdate.")
        elif pilihan == '3':
            new_negara = input("Masukkan negara baru: ")
            collection.update_one({"nama": nama}, {"$set": {"negara": new_negara}})
            print("negara berhasil diupdate.")
        else:
            print("Pilihan tidak valid.")
    else:
        print("Data tidak ditemukan.")
def hapus_data():
    nama = input("Masukkan produk yang ingin dihapus: ")
    result = collection.find_one({"nama": nama})
    if result:
        confirm = input(f"Apakah Anda yakin ingin menghapus data {result['nama']}? (y/n): ")
        if confirm.lower() == 'y':
            collection.delete_one({"nama": nama})
            print("Data berhasil dihapus.")
        else:
            print("Penghapusan dibatalkan.")
    else:
        print("Data tidak ditemukan.")
def menu():
    while True:
        print("\nMenu:")
        print("1. Tambah Data")
        print("2. Cari Data Berdasarkan Nama")
        print("3. Update Data Berdasarkan Nama")
        print("4. Hapus Data Berdasarkan Nama")
        print("5. Keluar")
        
        pilihan = input("Pilih opsi (1/2/3/4/5): ")
        
        if pilihan == '1':
            tambah_data()
        elif pilihan == '2':
            cari_data()
        elif pilihan == '3':
            update_data()
        elif pilihan == '4':
            hapus_data()
        elif pilihan == '5':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
menu()
