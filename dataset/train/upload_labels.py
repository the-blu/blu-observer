# -*- coding: utf-8 -*-

import traceback
from util.urlutil import UrlUtil
from database.dataset import DataSet
from database.labels import Labels

LABEL_T = '__label__t'
LABEL_F = '__label__f'

urlUtil = UrlUtil()
dataset = DataSet()
labels = Labels()

def add_labels(label, data):
  print(data)
  if data is not None:
    for d in data:
      d['label'] = label
      labels.add_label(d)

def upload_t():
  try:
    offset = 0
    limit = 100
    while True:
      data = dataset.get_blacks(offset=offset, limit=limit)

      if len(data) == 0:
        break

      for i in data:
        lf = i.get('label_t', [])
        add_labels(LABEL_T, lf)

      offset = offset + limit
      print(offset)
  except Exception as ex:
    traceback.print_exc()
    print(ex)

def upload_f():
  try:
    offset = 2400
    limit = 100
    while True:
      data = dataset.get_whites(offset=offset, limit=limit)

      if len(data) == 0:
        break

      for i in data:
        lf = i.get('label_f', [])
        add_labels(LABEL_F, lf)

      offset = offset + limit
      print(offset)

  except Exception as ex:
    traceback.print_exc()
    print(ex)

if __name__ == '__main__':
  # upload_t()
  upload_f()
