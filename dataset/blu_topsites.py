from database.site import Site
TEXT_DATASET_FILE = './dataset/blu/blu_top_1000_sites.txt'

site = Site()

def main():
  try:
    text_dataset = open(TEXT_DATASET_FILE, 'r', encoding='UTF-8')
    i = 1
    for s in text_dataset.readlines():
      domain = s.replace('\n', '')
      res = site.add_topsite({'domain': domain, 'ranking': i, 'country': 'KR', 'src': 'blu'})
      i = i + 1
      print(res)
  except Exception as e:
    print(e)

if __name__ == '__main__':
  main()
