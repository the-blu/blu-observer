from database.observer import Observer

api = Observer()

domain = "facebook.com"

try:
  res = api.get_black(domain)
  print(res)
except Exception as e:
  print(e)
