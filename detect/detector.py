import os
from multiprocessing import Process, Value
import traceback
from util.urlutil import UrlUtil
from capture.har import Har
from database.observer import Observer

class Detector(object):
  def __init__(self, dataset):
    super(Detector,self).__init__()
    self.process = None
    self.urlUtil = UrlUtil()
    self.har = Har()

  def run(self, observer_id, url, language):
    self.process = Process(target=self.detect, args=(observer_id, url, language,))
    self.process.start()
    self.process.join(60)

  def detect(self, observer_id, url, language):
    origin = self.urlUtil.get_origin(url)

    data = self.har.capture(url)
    # print(data)

    try:
      entries = data['log']['entries']
      observer = Observer()

      for entry in entries:
        req = entry['request']
        req_url = req['url']
        req_origin = self.urlUtil.get_origin(req_url)

        info = self.urlUtil.url_parse(req_url)
        info['query_string'] = req.get('queryString', {})

        if origin != req_origin:
          black = observer.get_black(sub_domain=info['sub_domain'], src='blu')

          if black == None:
            b = observer.get_black(domain=req_origin)
            if b != None:
              whites = b.get('whites', [])
              if origin in whites:
                print('is white')
            else:
              n = observer.get_normal(info['sub_domain'])
              if n == None:
                gray = {
                  'url': req_url,
                  'observer_id': observer_id,
                  'sub_domain': info['sub_domain'],
                  'domain': req_origin,
                  'observer_url': url,
                  'path': info['path'],
                  'query_string': info['query_string'],
                  'language': language
                }
                observer.add_gray(gray)
          # else:
          #   whites = black.get('whites', [])
            # if origin in whites:
            #   print('is white')
            # else:
            #   print('is black: ' + req_origin)
        # else:
        #   print('is origin: ' + req_origin)
    except Exception as e:
      print(e)

    data = {
      'status': 'done'
    }
    observer.update_observer(observer_id, data)
