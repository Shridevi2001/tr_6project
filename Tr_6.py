import pymongo
from pylogix import PLC

client = client=pymongo.MongoClient("mongodb://localhost:27017/")

databaselist = client.list_database_names()

if "TR6pro" in databaselist:
    print("databasse exist")

else:
    databasename = client["TR6pro"]
    collection = databasename.create_collection("Status")
    document = {"_id":"12345"}
    collection.insert_one(document)

databasename = client["TR6pro"]
x = databasename.get_collection("Status")
taglist = ["CurrentScreen","Zone1ASpeed","Zone2ASpeed","Zone2BSpeed"]
global comm
with PLC() as comm:
    comm.IPAddress = '192.168.1.9'
    ret = comm.Read(taglist)
    for i in taglist:
        if i == "CurrentScreen":
            ret1 = comm.Read("CurrentScreen")
            x.update_one({"_id":"12345"},{"$set":{"CurrentScreen":ret1.Value}})

        elif i == "Zone1ASpeed":
            ret2 = comm.Read("Zone1ASpeed")
            x.update_one({"_id":"12345"},{"$set":{"Zone1ASpeed":ret2.Value}})
        
        elif i == "Zone2ASpeed":
            ret3 = comm.Read("Zone2ASpeed")
            x.update_one({"_id":"12345"},{"$set":{"Zone2ASpeed":ret3.Value}})

        else:
            ret4 = comm.Read("Zone2BSpeed")
            x.update_one({"_id":"12345"},{"$set":{"Zone2BSpeed":ret4.Value}})

print("========== END ==========")