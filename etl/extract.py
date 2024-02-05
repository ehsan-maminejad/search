import pandas as pd
import os
import sys
from utils.mongo import Mongo

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_path)

class PostModel(Mongo):
    _connection_name = 'mongo_connection1'
    _collection_name = 'post'
    _db_name = 'data_pipline'


class CategoriesConfigModel(Mongo):
    _connection_name = 'mongo_connection1'
    _collection_name = 'categories'
    _db_name = 'app_config'


class ColorsConfigModel(Mongo):
    _connection_name = 'mongo_connection1'
    _collection_name = 'colors'
    _db_name = 'app_config'


class MaterialsConfigModel(Mongo):
    _connection_name = 'mongo_connection1'
    _collection_name = 'materials'
    _db_name = 'app_config'


class brandsConfigModel(Mongo):
    _connection_name = 'mongo_connection1'
    _collection_name = 'brands'
    _db_name = 'app_config'


class AttributesConfigModel(Mongo):
    _connection_name = 'mongo_connection1'
    _collection_name = 'attributes'
    _db_name = 'app_config'


class StopWordsConfigModel(Mongo):
    _connection_name = 'mongo_connection1'
    _collection_name = 'search_stop_words'
    _db_name = 'app_config'


class ConfigModel(Mongo):
    _connection_name = 'mongo_connection1'
    _collection_name = 'classified_categories'
    _db_name = 'app_config'



def prepare_config(model, query={}):
    config_list = []
    records = model.collection.find(query)
    for doc in records:
        config_list.append(doc)
    config = pd.DataFrame(config_list)
    config.drop(columns=['_id'], inplace=True)
    return config



def prepare_config_ids():
    classified_categorys = {}
    classified_category_model = ConfigModel()
    classified_categorys_records = classified_category_model.collection.find({})
    for doc in classified_categorys_records:
        classified_categorys.update({
            doc['key']: doc['values']
        })
    return classified_categorys

def get_stop_words():
    with open(f'{root_path}/persian', encoding='utf-8') as f:
        content = f.read()
        stop_words = content.split()
    return stop_words


classified_categorys = prepare_config_ids()
category = prepare_config(CategoriesConfigModel())
material = prepare_config(MaterialsConfigModel())
brand = prepare_config(brandsConfigModel())
attribute = prepare_config(AttributesConfigModel(), query={"service": "title"})
color = prepare_config(ColorsConfigModel(), query={"service": "title"})
# stop_words = get_stop_words()
stop_words = prepare_config(StopWordsConfigModel())
