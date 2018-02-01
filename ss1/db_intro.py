from pymongo import MongoClient

mongo_uri = "mongodb://taken_the_death:02103845367p@ds119088.mlab.com:19088/taken_the_death"
#1. mo ra ket noi data base
clinet = MongoClient(mongo_uri)
#2. lay datebase ra
db = client.get_default_database()
#3. lay colection
games = db ['games']
#4.create a new document
# new_game = {
#     'title':'LOL',
#      "description" : "MOBA game"
# }
#5. nhet colection vao dtbase
# games.insert_one(new_game)
#
# blog = db['blog']
# new_blog = {
#     'title': 'Thoi thanh xuan da qua',
#     'description': 'truyen cho tuoi teen'
# }
# blog.insert_one(new_blog)

game_list = games.find()

for game in game_list:
    print(game['title'])
