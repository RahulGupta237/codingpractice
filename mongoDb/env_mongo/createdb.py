import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
print("*****************Create Database****************************************")
mydb = myclient["pip_task"]
print(mydb)

print()
print("**************show list of database****************")
print(myclient.list_database_names())


