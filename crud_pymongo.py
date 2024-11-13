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
