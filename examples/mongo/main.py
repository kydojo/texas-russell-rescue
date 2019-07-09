import os

from pymongo import MongoClient
password = os.environ['MONGO_DB_PW']
conn_string = "mongodb+srv://slucas:" + password + "@my-cluster-sample-fung5.mongodb.net/test?retryWrites=true&w=majority"
client = MongoClient(conn_string)

# access a specific db and if not exists, create it
db = client.pymongo_test

# create a new document
posts = db.posts
post_data = {
    'title': 'python and mongodb',
    'content': 'pymongo is fun',
    'author': 'shannon'
}

# add the data
result = posts.insert_one(post_data)

# print the id that entered it into the table
print(result.inserted_id)

my_post = posts.find_one({'author':'shannon'})
print(my_post)
# this prints the object_id and not the inserted_id
print(my_post['_id'])

