#!/usr/bin/env python3

import datetime
import os
from pydblite import Base
from sys import stdin

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))

def save_in_db(comic_url):
    db = Base(os.path.join(SCRIPT_DIR, 'comics.db'))
    db.create('comic', 'time', mode="open")

    db.insert(comic=comic_url, time=datetime.datetime.now())
    db.commit()

    return len(db(comic=comic_url)) == 1

def main():
  comic_url = stdin.readline()
  if save_in_db(comic_url):
      print(comic_url)

if __name__ == '__main__':
    main()

