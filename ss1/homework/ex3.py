from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)
db = client.get_default_database()

posts = db ['posts']
new_post = {
    'title':'The last time',
    'author':'Ngọc Phúc',
    'content':'''“Cause you never think that the last time is the last time. You think there will be more. You think you have forever, but you don’t.”'''

}

posts.insert_one(new_post)
