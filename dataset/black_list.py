import json

class BlackList(object):
  def __init__(self):
    super(BlackList,self).__init__()
    with open('disconnect/blacklist.json') as f:
      data = json.load(f)

    categories = data['categories']
    self.black_list = []

    for category in categories:
      c = categories[category]
      for host in c:
        l = self.get_hosts(host)
        self.black_list.extend(l)


  def get_hosts(self, data):
    if isinstance(data, dict):
      for d in data:
        return self.get_hosts(data[d])
    elif isinstance(data, list):
      return data
    else:
      return None

  def get_list(self):
    return self.black_list
