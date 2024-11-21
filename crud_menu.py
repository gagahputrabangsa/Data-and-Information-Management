import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["prak8"]
collection = db["MK"]

def tambah_data():
    nama = input("Masukkan nama produk: ")
    harga = int(input("Harga: "))
    negara = input("Dari Negara Mana: ")
    data = {"nama": nama, "harga": harga, "negara":negara}
    result = collection.insert_one(data)
    print("Data berhasil ditambahkan dengan ID:", result.inserted_id)
    
def update_data():
    nama = input("Masukkan produk yang ingin diupdate: ")
    result = collection.find_one({"nama": nama})
    if result:
        print("\nData ditemukan:")
        print("Nama:", result['nama'])
        print("Harga:", result['harga'])
        print("Negara:", result['negara'])

        pilihan = input("Apakah Anda ingin mengupdate: \n(1) Nama\n(2) Harga\n(3) Negara\nPilih (1/2/3): ")
