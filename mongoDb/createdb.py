import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
print("*****************Create Database****************************************")
mydb = myclient["pip_task"]
print(mydb)

print()
print("**************show list of database****************")
# Get a list of the available databases
db_list = myclient.list_database_names()
print(db_list)
# Print the list of databases
for db in db_list:
    print(db)


print("*********** Create collection******************")

mycol = mydb["customers"]

print("*********** Insert Record into  collection******************")

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)
print(x)

print(x.inserted_id) # return the id field


print("**********8888Insert multiple data into collection***************")

mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)
print()
print("**************find one and find all like select * mysql ************ ")

x = mycol.find_one()

print(x)


for i in mycol.find():
    print(x)
print()
print("finde for specific field with include 1")

for x in mycol.find({},{"address": 1 }):
  print(x)


print()
print("************** find items with exclude 0**************")
for x in mycol.find({},{ "address": 0 }):
  print(x)


print()


print("***********8Check if collection exist*************")
collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.")
for i in collist:
    print(i)


print()
print("*************** Filtering Result through specific items *****************8")
myquery = { "address": "Park Lane 38" }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)

print()

print("**** filter with advance query object*********")

myquery = { "address": { "$gt": "S" } }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)

print()

print("**** filter with Regular expression*********")

myquery = { "address": { "$regex": "^S" } }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)



print()
print("********Sorting****sort(name, 1) #ascending and sort(name, -1) #descending*************")

print()
mydoc = mycol.find().sort("name",-1)

for x in mydoc:
  print(x)



print()

print("********Update record*************")

print()

myquery = { "address": "Canyon 123" }
newvalues = { "$set": { "address": "Solver Rahul" } }

mycol.update_one(myquery, newvalues)

#print "customers" after the update:
for x in mycol.find():
  print(x)



print()

print("********Update Multiple  record*************")

print()


myquery = { "address": { "$regex": "^S" } }
newvalues = { "$set": { "name": "Minnie" } }

x = mycol.update_many(myquery, newvalues)

print(x.modified_count, "documents updated.")


print()

print("********Limit record*************")

print()


myresult = mycol.find().limit(5)

#print the result:
for x in myresult:
  print(x)
print("Hi please refer w3 school for delete and many delete like find")
# drop table or collection
#delete record
# update record
#limit 

