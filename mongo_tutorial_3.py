from pymongo import MongoClient

client  = MongoClient('localhost', 27017)

mydb = client.test_database


import datetime

post = {
	"author":"Duke5",
	"title": "Pymongo 101 -5",
	"tags" : ["MongoDB 5", "Pymongo 101 - A5", "Tutorual 5"],
	"date" : datetime.datetime.utcnow()
	}

posts = mydb.posts
postid = posts.insert(post)

mydb.posts.drop()

print postid
print mydb.collection_names()

new_posts = [{"author": "Duke 6",
              "title" : "PyMongo 101-A6",
              "tags" : ["MongoDB 6", "PyMongo 6", "Tutorial 6"],
              "date" : datetime.datetime(2015, 11, 28, 01, 13)},
             {"author": "Adja",
              "title": "MongoDB 101-A7",
              "note": "Schema free MongoDB",
              "date": datetime.datetime(2015, 11, 29, 11, 42)}
            ]

posts.insert(new_posts)       




for post in posts.find({"date": {"$lt": datetime.datetime(2015, 12, 1)}}).sort("author"):
	print post