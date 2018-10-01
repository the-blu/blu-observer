import json
from database.observer import Observer

observer = Observer()
files = ['blu/ko.json', 'blu/en.json', 'blu/vi.json', 'blu/id.json']


def upload(file):
  with open(file) as f:
    data = json.load(f)
    domains = data.keys()

    for b in domains:
      res = observer.add_black({'domain': b.replace('?', '.'), 'src': 'blu'})
      print(res)

def main():
  for f in files:
    upload(f)

if __name__ == '__main__':
  main()

