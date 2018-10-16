from database.observer import Observer
from dataset.black_list import BlackList
from dataset.white_list import WhiteList

observer = Observer()

black = BlackList()
white = WhiteList()

bl = black.get_list()
wl = white.get_list()

for b in bl:
  res = observer.add_black({'sub_domain': b, 'src': 'disconnect'})
  print(res)

for w in wl:
  resources = wl[w]
  for resource in resources:
    res = observer.add_white(resource, w)
    print(w, res)
