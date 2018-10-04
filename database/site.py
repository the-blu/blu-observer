from database.db import DataBase

class Site(DataBase):
  def __init__(self):
      super(Site,self).__init__()
      self.topsites = self.db.topsites

  def add_topsite(self, site):
    res = {'result': 'success',
           'message': None}

    query = {"domain": site.get('domain', None),
             "country": site.get('country', None)}
    r = self.topsites.update_one(query,
                                 {"$set": site},
                                 upsert=True)

    if 'upserted' in r.raw_result:
      res['message'] = "created"
    else:
      res['message'] = "existing"

    return res

  def get_sites(self,
                country=None,
                language=None,
                src=None,
                offset=0, limit=100):
    query = {}

    if country != None:
      query['country'] = country

    if language != None:
      query['language'] = language

    if src != None:
      query['src'] = src

    sort = [('ranking', 1)]

    try:
      r = self.topsites.find(query).sort(sort).skip(offset).limit(limit)
    except Exception as e:
      print(e)

    return list(r)

