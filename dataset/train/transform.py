# -*- coding: utf-8 -*-
import re
from util.urlutil import UrlUtil

class Transform(object):
  def __init__(self):
    super(Transform,self).__init__()
    self.urlUtil = UrlUtil()
    with open("./dataset/train/except_words.dat") as f1:
      self.words = [line.strip() for line in f1]
    with open("./dataset/train/except_keywords.dat") as f2:
      self.keywords = [line.strip() for line in f2]

  def clean(self, data):
    sentence = []
    sub_domain = data.get('sub_domain', None)
    sub_domain_name = self.urlUtil.remove_tld(sub_domain)
    # print(sub_domain_name)
    sentence.extend(sub_domain_name.split('.'))
    path = data.get('path', None)
    path = path.lower()
    # self.normalize(path)
    # sentence.extend(path.split('/'))
    if self.is_normal_content(path) is False:
      path = self.remove_digits(path)
      paths = self.split_path(path)
      paths = self.remove_value(paths)
      # print(paths)
      sentence.extend(paths)

    sentence = list(filter(None, sentence))
    self.remove_except_words(sentence)
    self.remove_except_keywords(sentence)
    return sentence

  def remove_except_words(self, data):
    for word in self.words:
      if word in data:
        data.remove(word)

  def remove_except_keywords(self, data):
    for word in self.keywords:
      for d in data:
        if d.find(word) > -1:
          data.remove(d)

  def remove_digits(self, s):
    return ''.join([i for i in s if not i.isdigit()])

  def remove_value(self, paths):
    p = []
    for s in paths:
      s = s.split('=')[0]
      p.append(self.replace_percent(s))
    return p

  def split_path(self, s):
    return s.split('/')

  def is_normal_content(self, s):
    s = s.lower()
    ext = [".jpg", ".jpg_s", ".jpeg", ".css", ".html", ".gif", ".gif_s", \
           ".png", ".png_s", ".swf", ".svg", ".wmv", ".ttf", ".woff", ".woff2"]
    return s.endswith(tuple(ext))

  def replace_percent(self, s):
    return s.replace('%', ' ')

  def normalize(self, s):
    s = s.lower()
    # Replace ips
    s = re.sub(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', ' _ip_ ', s)
    # Isolate punctuation
    s = re.sub(r'([\'\"\.\(\)\!\?\-\\\/\,])', r' \1 ', s)
    # Remove some special characters
    s = re.sub(r'([\;\:\|•«\n])', ' ', s)
    # Replace numbers and symbols with language
    s = s.replace('&', ' and ')
    s = s.replace('@', ' at ')
    return s
