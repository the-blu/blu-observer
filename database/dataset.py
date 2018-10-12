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


  def get_data(self, data, src=None):
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

