#!/usr/bin/env python3

import os
from pydblite import Base
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))

def list_comics():
    db = Base(os.path.join(SCRIPT_DIR, 'comics.db'))
    db.create('comic', 'time', mode="open")
    for l in db:
        print('%s %s' % (l['comic'], l['time']))

def main():
    list_comics()

if __name__ == '__main__':
    main()

