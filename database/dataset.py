from bson.objectid import ObjectId
from database.db import DataBase

class DataSet(DataBase):
  def __init__(self):
      super(DataSet,self).__init__()
      self.dataset = self.db.dataset

  def add_data(self, data):
    res = {'result': 'success',
           'message': None}

    query = {}

    host = data.get('host', None)
    path = data.get('path', None)

    if host != None:
      query['host'] = host

    if path != None:
      query['path'] = path

    r = self.dataset.update_one(query,
                                 {"$set": data},
                                 upsert=True)

    if 'upserted' in r.raw_result:
      res['message'] = "created"
    else:
      res['message'] = "existing"

    return res


  def get_datum(self, data, src=None):
    query = {}

    query = {}

    host = data.get('host', None)
    path = data.get('path', None)

    if host != None:
      query['host'] = host

    if path != None:
      query['path'] = path

    try:
      r = self.dataset.find_one(query)
    except Exception as e:
      print(e)

    return r

  def get_data(self,
              offset=0, limit=100):
    query = {}
    projection = {}

    try:
      r = self.dataset.find(query, projection).skip(offset).limit(limit)
    except Exception as e:
      print(e)

    return list(r)

  def get_blacks(self,
                 domain=None,
                 sub_domain=None,
                 language=None,
                 path=None,
                 src=None,
                 offset=0, limit=100):
    query = {}

    if domain != None:
      query['domain'] = domain

    if sub_domain != None:
      query['sub_domain'] = sub_domain

    if path != None:
      query['path'] = path

    if language != None:
      query['language'] = language

    if src != None:
      query['src'] = src

    projection = {
      'label_t': 1
    }

    try:
      r = self.dataset.find(query, projection).skip(offset).limit(limit)
    except Exception as e:
      print(e)

    return list(r)

  def get_whites(self,
                 domain=None,
                 sub_domain=None,
                 language=None,
                 path=None,
                 src=None,
                 offset=0, limit=100):
    query = {}

    if domain != None:
      query['domain'] = domain

    if sub_domain != None:
      query['sub_domain'] = sub_domain

    if path != None:
      query['path'] = path

    if language != None:
      query['language'] = language

    if src != None:
      query['src'] = src

    projection = {
      'label_f': 1
    }

    try:
      r = self.dataset.find(query, projection).skip(offset).limit(limit)
    except Exception as e:
      print(e)

    return list(r)
