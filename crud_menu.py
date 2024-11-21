import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["prak8"]
collection = db["MK"]
def update_data():
    nama = input("Masukkan produk yang ingin diupdate: ")
    result = collection.find_one({"nama": nama})
    if result:
        print("\nData ditemukan:")
        print("Nama:", result['nama'])
        print("Harga:", result['harga'])
        print("Negara:", result['negara'])

        pilihan = input("Apakah Anda ingin mengupdate: \n(1) Nama\n(2) Harga\n(3) Negara\nPilih (1/2/3): ")
