# -*- coding: utf-8 -*-
from urllib.parse import urlparse
from tld import get_tld, get_fld

class UrlUtil(object):
  def __init__(self):
    super(UrlUtil,self).__init__()
    self.tlds = None

  def load_tlds(self):
    with open("./util/effective_tld_names.dat") as tld_file:
      self.tlds = [line.strip() for line in tld_file if line[0] not in "/\n"]

  def get_origin(self, url):
    origin = get_fld(url, fix_protocol=True)
    return origin

  def url_parse(self, url):
    if url.startswith('http') != True:
      url = 'http://' + url
    u = urlparse(url)
    d = {}
    d['sub_domain'] = u.netloc
    d['path'] = u.path
    return d

  def remove_tld(self, url):

    if self.tlds is None:
      self.load_tlds()
    url = url.split(':')[0]

    if url.startswith('http') != True:
      url = 'http://' + url
    a = urlparse(url)
    # print(a)
    # print(a[1])
    url_elements = a[1].split('.')
    # url_elements = ["abcde","co","uk"]

    for i in range(-len(url_elements), 0):
      last_i_elements = url_elements[i:]
      # print(last_i_elements)
      candidate = ".".join(last_i_elements)  # abcde.co.uk, co.uk, uk

      # print(self.tlds)
      if (candidate in self.tlds):

        r = ".".join(url_elements[:i])

        return r

  # def get_domain(self, url):
  #   if url.startswith('http') != True:
  #     url = 'http://' + url
  #
  #   a = urlparse(url)
  #   url_elements = a[1].split('.')
  #   # url_elements = ["abcde","co","uk"]
  #
  #   for i in range(-len(url_elements), 0):
  #     last_i_elements = url_elements[i:]
  #     #    i=-3: ["abcde","co","uk"]
  #     #    i=-2: ["co","uk"]
  #     #    i=-1: ["uk"] etc
  #
  #     candidate = ".".join(last_i_elements)  # abcde.co.uk, co.uk, uk
  #     wildcard_candidate = ".".join(["*"] + last_i_elements[1:])  # *.co.uk, *.uk, *
  #     exception_candidate = "!" + candidate
  #
  #     # match tlds:
  #     if (exception_candidate in self.tlds):
  #       return ".".join(url_elements[i:])
  #     if (candidate in self.tlds or wildcard_candidate in self.tlds):
  #       return ".".join(url_elements[i - 1:])
  #       # returns "abcde.co.uk"
  #
  #   raise ValueError("Domain not in global list of TLDs")

