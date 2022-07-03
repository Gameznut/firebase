import os

import pymongo
import hashlib, os, binascii

client = pymongo.MongoClient()

myDb = client["python"]

myCol = myDb["people"]


# data = {
#     "name": "Emmanuel",
#     "age": 12
# }
# insert one
# myCol.insert_one(data)

# datas = [
#     {
#         "name": "Ayo",
#         "age": 12
#     },
#     {
#         "name": "Paula",
#         "age": 14
#     }
# ]
# insert many
# id = myCol.insert_many(datas)
# print(id.inserted_ids)

# See available database
# print(client.list_database_names())

# collection name in a specific database
# print(myDb.list_collection_names())

# getting all data in a collection
# for x in myCol.find():
#     print(x)

# getting all data in a collection
# for x in myCol.find():
# printing out each values for name
#     print(x["name"])

# getting all data less than a number in a collection
# for x in myCol.find({"age": {"$lte": 12}}):
#     print(x)

def hash_password(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode("ascii")
    password_hash = hashlib.pbkdf2_hmac("sha512", password.encode("utf-8"), salt, 100000)
    password_hash = binascii.hexlify(password_hash)
    return (salt + password_hash).decode("ascii")


def check_password(stored_password, userPassword):
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    password_hash = hashlib.pbkdf2_hmac("sha512", userPassword.encode("utf-8"), salt.encode("ascii"), 100000)
    password_hash = binascii.hexlify(password_hash).decode("ascii")
    return password_hash == stored_password


email = input("Enter your email: ")
password = input("Enter your password: ")
passwordHashed = hash_password(password)
check = check_password(passwordHashed, password)
user = {
    "email": email,
    "password": passwordHashed
}

# # is the same as
# # users = []
# # users.append(user)
# # users = [user]
# # myDb.create_collection("users")

myCol2 = myDb["users"]
myCol2.insert_one(user)
myquery = { "email": "ram" }
for x in myCol2.find(myquery):
    passwordHashed = x["password"]
    check = check_password(passwordHashed, "3")
    #
    print(check)
    print(passwordHashed)

