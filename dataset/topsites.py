import os
from dataset.alexa import AlexaTop
from database.site import Site

ACCESS_KEY_ID = os.environ['ACCESS_KEY_ID']
SECRET_ACCESS_KEY = os.environ['SECRET_ACCESS_KEY']

site = Site()
alexa = AlexaTop(ACCESS_KEY_ID, SECRET_ACCESS_KEY)

countries = ['KR', 'US', 'VN', 'ID']

def upload(ranking, country):
  for r in ranking:
    res = site.add_topsite({'domain': ranking[r], 'ranking': r, 'country': country})
    print(res)

def main():
  for c in countries:
    ranking = alexa.get_sites(c, start=1001, count=10000)
    upload(ranking, c)

if __name__ == '__main__':
  main()
