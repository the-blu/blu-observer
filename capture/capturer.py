import os
from multiprocessing import Process, Value
import traceback
from util.urlutil import UrlUtil
from capture.har import Har
from database.dataset import DataSet
from database.observer import Observer

class Capturer(object):
  def __init__(self):
    super(Capturer,self).__init__()
    self.process = None
    self.urlUtil = UrlUtil()
    self.har = Har()

  def run(self, url):
    self.process = Process(target=self.capture, args=(url,))
    self.process.start()
    self.process.join(60)

  def kill_headless(self):
    os.kill(self.process.pid)

  def capture(self, url):
    try:
      origin = self.urlUtil.get_origin(url)
      p = self.urlUtil.url_parse(url)

      label = {
        'host': p['sub_domain'],
        'path': p['path'],
        'label_f': None,
        'label_t': None
      }

      label_t = []
      label_f = []

      data = self.har.capture(url)

      entries = data['log']['entries']

      for entry in entries:
        info = {
          'sub_domain': None,
          'path': None,
          'query_string': None
        }
        observer = Observer()

        req = entry['request']
        url = req['url']
        req_origin = self.urlUtil.get_origin(url)

        info = self.urlUtil.url_parse(url)
        info['query_string'] = req.get('queryString', {})

        if origin != req_origin:
          # print('req_origin', req_origin)
          # print('sub_comain', sub_domain)
          black = observer.get_black(req_origin)

          if black == None:
            b = observer.get_black(info['sub_domain'], src='blu')
            if b != None:
              whites = b.get('whites', [])
              if origin in whites:
                # print('white 1')
                label_t.append(info)
              else:
                label_f.append(info)
          else:
            whites = black.get('whites', [])
            if origin in whites:
              # print('white 2')
              label_t.append(info)
            else:
              label_f.append(info)
        else:
          label_t.append(info)

      label['label_t'] = label_t
      label['label_f'] = label_f

      dataset = DataSet()
      dataset.add_data(label)
    except Exception as e:
      traceback.print_exc()
