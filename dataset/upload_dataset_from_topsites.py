# -*- coding: utf-8 -*-

import traceback
from capture.chrome import Chrome
from database.site import Site
from util.urlutil import UrlUtil
from database.dataset import DataSet
from capture.capturer import Capturer

COUNTRIES = ['KR', 'US', 'VN', 'ID']

urlUtil = UrlUtil()
site = Site()
chrome = Chrome()
dataset = DataSet()
capturer = Capturer()

def validate_site(url):
  p = urlUtil.url_parse(url)
  host = p['sub_domain']
  path = p['path']

  data = {}
  data['host'] = host
  data['path'] = path
  res = dataset.get_datum(data)

  if res == None:
    return True
  else:
    return False

if __name__ == '__main__':

  chrome.run()
  try:
    for c in COUNTRIES:
      offset = 0
      limit = 100
      while True:
        sites = site.get_sites(country=c, offset=offset, limit=limit)

        if len(sites) == 0:
          break

        offset = offset + limit

        for s in sites:
          if validate_site(s['domain']):
            capturer.run(s['domain'])

  except Exception as ex:
    traceback.print_exc()
    print(ex)
