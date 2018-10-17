# -*- coding: utf-8 -*-

import traceback
from util.urlutil import UrlUtil
from database.labels import Labels
from dataset.train.transform import Transform

LABEL_T = '__label__t'
LABEL_F = '__label__f'


urlUtil = UrlUtil()
transform = Transform()
labels = Labels()
fl = open('make_train.txt','w')

def make_text(data):

  text,l = transform.clean(data)

  print(l)
  if not text:
    pass
  else:
    fl.write(l + ' ')
    for i in text:
      fl.write(i+' ')
    fl.write('\n')
    print(text)


  return None

def generate():
  try:
    offset = 0
    limit = 100
    with open('labled_dataset.dat', 'w') as f:
      while True:
        data = labels.get_labels(offset=offset, limit=limit)

        if len(data) == 0:
          break

        for d in data:
          t = make_text(d)
          # print(t)
          # f.write(t)

        offset = offset + limit

  except Exception as ex:
    traceback.print_exc()
    print(ex)

  f.close()

if __name__ == '__main__':
  generate()
