# -*- coding: utf-8 -*-

import redis
import os
import traceback
import json
from tld import get_tld, get_fld
from multiprocessing import Process
from urllib.parse import urlparse
from capture.har import Har
from capture.chrome import Chrome
from database.observer import Observer
from detect.detector import Detector

REDIS_SERVER = os.environ['REDIS_SERVER']
REDIS_PASSWORD = os.environ['REDIS_PASSWORD']
REDIS_TOPIC_OBSERVER_URLS = os.environ['REDIS_TOPIC_OBSERVER_URLS']
redis = redis.StrictRedis(host=REDIS_SERVER, password=REDIS_PASSWORD)

har = Har()
observer = Observer()
chrome = Chrome()
detector = Detector(observer)

def get_origin(url):
  if url.startswith('http'):
    origin = get_fld(url)
  else:
    origin = get_fld('http://' + url)
  return origin

# def do_observe(id, observer_url, language):
#
#   origin = get_origin(observer_url)
#
#   data = har.capture(observer_url)
#   # print(data)
#
#   try:
#     entries = data['log']['entries']
#
#     for entry in entries:
#       req = entry['request']
#       req_url = req['url']
#       req_origin = get_fld(req_url)
#
#       u = urlparse(req_url)
#       req_sub_domain = u.netloc
#       req_path = u.path
#       req_query_string = req.get('queryString', {})
#
#       if origin != req_origin:
#         black = observer.get_black(sub_domain=req_sub_domain, src='blu')
#
#         if black == None:
#           b = observer.get_black(domain=req_origin)
#           if b != None:
#             whites = b.get('whites', [])
#             if origin in whites:
#               print('is white')
#           else:
#             n = observer.get_normal(req_sub_domain)
#             if n == None:
#               gray = {
#                 'url': req_url,
#                 'observer_id': id,
#                 'sub_domain': req_sub_domain,
#                 'domain': req_origin,
#                 'observer_url': observer_url,
#                 'path': req_path,
#                 'query_string': req_query_string,
#                 'language': language
#               }
#               observer.add_gray(gray)
#         else:
#           whites = black.get('whites', [])
#           if origin in whites:
#             print('is white')
#           else:
#             print('is black: ' + req_origin)
#       else:
#         print('is origin: ' + req_origin)
#   except Exception as e:
#     print(e)
#
#   data = {
#     'status': 'done'
#   }
#   observer.update_observer(id, data)

def register(url, language):
  u = urlparse(url)
  sub_domain = u.netloc
  path = u.path

  data = {
    'url': url,
    'sub_domain': sub_domain,
    'path': path,
    'language': language,
    'status': 'doing'
  }
  res = observer.add_observer(data)

  if res['message'] is 'created':
    return res['id']
  else:
    return None

if __name__ == '__main__':
  chrome.run()

  while True:
    try:
      task_code, task_data = redis.blpop([REDIS_TOPIC_OBSERVER_URLS], 0)
      if task_data:
        urlData = task_data.decode("utf-8")
        urlObj = json.loads(urlData)
        if urlObj is not None:
          url = urlObj.get('url', None)
          if url is not None:
            language = urlObj['language']
            id = register(url, language)
            if id is not None:
              detector.run(id, url, language)

    except Exception as ex:
      traceback.print_exc()
      print(ex)
