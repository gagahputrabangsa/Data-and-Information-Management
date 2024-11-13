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
