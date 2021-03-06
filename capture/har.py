import os
import json
from urllib.parse import urlencode
import tempfile

UA = "'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36'"

BASE_DIR = './capture/har'

class Har(object):
  def __init__(self):
    super(Har,self).__init__()

  def capture(self, url):
    if os.path.exists(BASE_DIR) is False:
      os.mkdir(BASE_DIR)

    if url.startswith('http'):
      u = url
    else:
      u = 'http://' + url

    self.temp_file = tempfile.mktemp()
    print(self.temp_file)

    url = u.replace('&', '\&')
    cmd = 'chrome-har-capturer -p 9222 -o %s %s -a %s' % (self.temp_file, url, UA)
    os.system(cmd)

    if os.path.exists(self.temp_file) is True:
      print('success')
      with open(self.temp_file, 'r', encoding='utf-8') as f:
        har = json.load(f)
        self.clear()
        return har
    else:
      print('fail')
      self.clear()
      return None

  def clear(self):
    os.remove(self.temp_file)
