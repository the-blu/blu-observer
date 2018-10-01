from database.db import DataBase

class Observer(DataBase):
  def __init__(self):
      super(Observer,self).__init__()
      self.blacks = self.db.blacks
      self.whites = self.db.whites

  def add_black(self, black):
    res = {'result': 'success',
           'message': None}

    query = {"domain": black.get('domain', None)}
    r = self.blacks.update_one(query,
                                 {"$set": black},
                                 upsert=True)

    if 'upserted' in r.raw_result:
      res['message'] = "created"
    else:
      res['message'] = "existing"

    return res

  def add_white(self, black, white):
    query = {"domain": black}
    r = self.blacks.update_one(query,
                               {"$addToSet": {
                                 'whites': white
                               }},
                               upsert=True)

  def get_black(self, domain, src=None):
    query = {}
    query['domain'] = domain

    if src != None:
      query['src'] = src

    try:
      r = self.blacks.find_one(query)
    except Exception as e:
      print(e)

    return r
