import json

class WhiteList(object):
  def __init__(self):
    super(WhiteList,self).__init__()
    with open('disconnect/whitelist.json') as f:
      data = json.load(f)

    self.white_list = {}

    for category in data:
      properties = data[category]['properties']
      resources = data[category]['resources']
      for property in properties:
        self.white_list[property] = resources

  def get_list(self):
    return self.white_list
