# -*- coding: utf-8 -*-

import traceback
from database.observer import Observer


observer = Observer()


def generate():
  try:
    offset = 0
    limit = 100
    while True:
      list = observer.get_observers(offset=offset, limit=limit)

      print(offset)
      if len(list) == 0:
        break

      for o in list:
        observer_id = str(o['_id'])
        grays = observer.get_grays(observer_id=observer_id)
        if len(grays) == 0:
          r = observer.delete_observer(observer_id)
          print(r)
        else:
          print('.')

      offset = offset + limit

  except Exception as ex:
    traceback.print_exc()
    print(ex)


if __name__ == '__main__':
  generate()
