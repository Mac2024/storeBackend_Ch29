import pymongo
import certifi


con_str = "mongodb+srv://Mac2084:Test1234@cluster0.4gcq6.mongodb.net/?retryWrites=true&w=majority"


client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())

db = client.get_database('Sports_Equipment')
