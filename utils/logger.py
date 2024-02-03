from utils.mongo import Mongo
from pymongo import InsertOne


class PostModel(Mongo):
    _connection_name = 'mongo_connection1'
    _collection_name = 'search'
    _db_name = 'logs'


def run(data):
    post_model = PostModel()
    operations = [InsertOne(data)]
    post_model.collection.bulk_write(operations)
