from bson.objectid import ObjectId
from database.db import DataBase

class Observer(DataBase):
  def __init__(self):
      super(Observer,self).__init__()
      self.blacks = self.db.blacks
      self.whites = self.db.whites
      self.grays = self.db.grays
      self.normals = self.db.normals
      self.observers = self.db.observers

  def add_black(self, black):
    res = {'result': 'success',
           'message': None}

    query = {"sub_domain": black.get('sub_domain', None)}
    r = self.blacks.update_one(query,
                                 {"$set": black},
                                 upsert=True)

    if 'upserted' in r.raw_result:
      res['message'] = "created"
    else:
      res['message'] = "existing"

    return res

  def add_observer(self, observer):
    res = {'result': 'success',
           'id': None,
           'message': None}

    query = {"sub_domain": observer['sub_domain'],
             "path": observer['path']}

    r = self.observers.update_one(query,
                                  {"$set": observer},
                                  upsert=True)

    if 'upserted' in r.raw_result:
      res['message'] = "created"
      res['id'] = str(r.raw_result['upserted'])
    else:
      res['message'] = "existing"

    return res

  def update_observer(self, id, observer):
    res = {'result': 'success',
           'message': None}

    query = {'_id': ObjectId(id)}

    r = self.observers.update_one(query,
                              {"$set": observer},
                              upsert=False)

    return r

  def add_gray(self, gray):
    res = {'result': 'success',
           'message': None}

    query = {'observer_id': gray['observer_id'],
             'sub_domain': gray['sub_domain']}

    gray['status'] = 'gray'

    r = self.grays.update_one(query,
                               {"$set": gray},
                               upsert=True)

    if 'upserted' in r.raw_result:
      res['message'] = "created"
    else:
      res['message'] = "existing"

    return res

  def add_white(self, black, white):
    query = {"sub_domain": black}
    r = self.blacks.update_one(query,
                               {"$addToSet": {
                                 'whites': white
                               }},
                               upsert=True)

  def get_black(self, domain=None, sub_domain=None, src=None):
    query = {}

    if domain != None:
      query['domain'] = domain

    if sub_domain != None:
      query['sub_domain'] = sub_domain

    if src != None:
      query['src'] = src

    try:
      r = self.blacks.find_one(query)
    except Exception as e:
      print(e)

    return r

  def get_normal(self, sub_domain, src=None):
    query = {}
    query['sub_domain'] = sub_domain

    if src != None:
      query['src'] = src

    try:
      r = self.normals.find_one(query)
    except Exception as e:
      print(e)

    return r

  def delete_gray(self, sub_domain):
    query = {
      'sub_domain': sub_domain
    }
    try:
      r = self.grays.delete_one(query)
    except Exception as e:
      print(e)
    return r.raw_result
