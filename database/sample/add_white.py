from database.observer import Observer

api = Observer()

black = 'www.xxx.com'
white = 'bbb.com'

try:
  res = api.add_white(black, white)
  print(res)
except Exception as e:
  print(e)
