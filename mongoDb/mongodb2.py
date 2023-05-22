import pymongo


# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["pip_task"]
collection = db["mycollection"]

# Get a list of unique values for a specific field
field_name = "myfield"
value_list = collection.distinct(field_name)

# Print the list of unique values
for value in value_list:
    print(value)
