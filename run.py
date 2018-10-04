# -*- coding: utf-8 -*-

import redis
import os
import traceback
from tld import get_tld, get_fld
from multiprocessing import Process
from urllib.parse import urlparse
from capture.har import Har
from capture.chrome import Chrome
from database.observer import Observer

REDIS_SERVER = os.environ['REDIS_SERVER']
REDIS_PASSWORD = os.environ['REDIS_PASSWORD']
REDIS_TOPIC_OBSERVER_URLS = os.environ['REDIS_TOPIC_OBSERVER_URLS']
redis = redis.StrictRedis(host=REDIS_SERVER, password=REDIS_PASSWORD)

har = Har()
observer = Observer()

def do_observe(id, observer_url):
  print('start observe : ' + observer_url)
  if observer_url.startswith('http'):
    origin = get_fld(observer_url)
  else:
    origin = get_fld('http://' + observer_url)

  data = har.capture(observer_url)
  # print(data)
  entries = data['log']['entries']

  for entry in entries:
    req = entry['request']
    req_url = req['url']
    req_origin = get_fld(req_url)

    u = urlparse(req_url)
    req_sub_domain = u.netloc
    req_path = u.path
    req_query_string = req.get('queryString', {})

    if origin != req_origin:
      black = observer.get_black(req_sub_domain, src='blu')

      if black == None:
        b = observer.get_black(req_origin)
        if b != None:
          whites = b.get('whites', [])
          if origin in whites:
            print('is white')
          else:
            gray = {
              'url': req_url,
              'observer_id': id,
              'sub_domain': req_sub_domain,
              'domain': req_origin,
              'observer_url': observer_url,
              'path': req_path,
              'query_string': req_query_string
            }
            observer.add_gray(gray)
      else:
        whites = black.get('whites', [])
        if origin in whites:
          print('is white')
        else:
          print('is black: ' + req_url)
    else:
      print('is origin: ' + req_url)

  data = {
    'status': 'done'
  }
  observer.update_observer(id, data)

def register(url):

  data = {
    'url': url,
    'status': 'doing'
  }
  res = observer.add_observer(data)

  if res['message'] is 'created':
    return res['id']
  else:
    return None

def run_chrome(arg):
  chrome = Chrome()
  while True:
    try:
      chrome.run_headless()
    except Exception as ex:
      traceback.print_exc()
      print(ex)

if __name__ == '__main__':
  Process(target=run_chrome, args=('',)).start()
  while True:
    try:
      task_code, task_data = redis.blpop([REDIS_TOPIC_OBSERVER_URLS], 0)
      if task_data:
        url = task_data.decode("utf-8")

        id = register(url)
        if id is not None:
          do_observe(id, url)

    except Exception as ex:
      traceback.print_exc()
      print(ex)
