from bson.objectid import ObjectId
from database.db import DataBase

class Labels(DataBase):
  def __init__(self):
      super(Labels,self).__init__()
      self.labels = self.db.labels

  def add_label(self, data):
    res = {'result': 'success',
           'message': None}

    query = {}

    sub_domain = data.get('sub_domain', None)
    path = data.get('path', None)
    label = data.get('label', None)

    if sub_domain != None:
      query['sub_domain'] = sub_domain

    if path != None:
      query['path'] = path

    if label != None:
      query['label'] = label

    r = self.labels.update_one(query,
                                 {"$set": data},
                                 upsert=True)

    if 'upserted' in r.raw_result:
      res['message'] = "created"
    else:
      res['message'] = "existing"

    return res

  def get_labels(self,
                 sub_domain=None,
                 path=None,
                 offset=0, limit=100):
    query = {}

    if sub_domain != None:
      query['sub_domain'] = sub_domain

    if path != None:
      query['path'] = path

    try:
      r = self.labels.find(query).skip(offset).limit(limit)
    except Exception as e:
      print(e)

    return list(r)
