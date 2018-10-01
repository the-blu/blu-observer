from database.observer import Observer

api = Observer()

black = {
  'domain': "www.xxx.com",
  'lang': "en",
  'whites': None
}

try:
  res = api.add_black(black)
  print(res)
except Exception as e:
  print(e)
