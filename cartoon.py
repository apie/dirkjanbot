#!/usr/bin/env python3

import requests
from lxml import html

def fetch_comic(link):
  page = requests.get(link).text
  doc = html.fromstring(page)
  link = doc.cssselect("article")[0]
  img = link.getchildren()[0]
  return img.attrib['src']

def main():
  url = 'http://www.dirkjan.nl'
  print(fetch_comic(url))

if __name__ == '__main__':
    main()

