from pymongo import MongoClient

#replace<uri> with your MongoDb Atlas connection string
uri = "mongodb+srv://Dashini:Dashini2023@cluster1.nf6jdn5.mongodb.net/"
client = MongoClient(uri)

#Replace <database-name> with the name of your database
db = client["Firstapp"]

#Replace <collection-name> with the name of your database
collection = db["Collect1"]

#check the connection
try:
    client.admin.command("ping")
    print("Pinnged your deployment.You successfully connected to MongoDB!")
except Exception as e:
    print(e)

document = {"name" : "Danial", "age": 36}

# Insert the document into the collection
insert_result = collection.insert_one(document)

#Print the ID of the inserted document
print("Inserted Document ID:",insert_result.inserted_id)
client.close()






