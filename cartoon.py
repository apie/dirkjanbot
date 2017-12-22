#!/usr/bin/env python3

import requests
from lxml import html

COMIC_PAGE = 'http://www.dirkjan.nl'

def fetch_comic():
  page = requests.get(COMIC_PAGE).text
  doc = html.fromstring(page)
  link = doc.cssselect("article")[0]
  img = link.getchildren()[0]
  return img.attrib['src']

def main():
  print(fetch_comic())

if __name__ == '__main__':
    main()

