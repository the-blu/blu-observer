import os
import json

UA = "'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36'"
BASE_DIR = './dataset/har'

class Har(object):
  def __init__(self):
    super(Har,self).__init__()

  def capture(self, site):
    if os.path.exists(BASE_DIR) is False:
      os.mkdir(BASE_DIR)

    cmd = 'chrome-har-capturer -p 9222 -o %s/%s.har http://%s -a %s' % (BASE_DIR, site, site, UA)
    os.system(cmd)

    har_file = '%s/%s.har' % (BASE_DIR, site)
    if os.path.exists(har_file) is True:
      print('success')
      with open(har_file, 'r') as f:
        har = json.load(f)
        return har
    else:
      print('fail')
      return None

  def clear(self, site):
    os.remove('%s/%s.har' % (BASE_DIR, site))
