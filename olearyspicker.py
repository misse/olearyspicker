#!/usr/bin/env python


"""
Pretty badass O'learys finder from long/lat and stuff.

Usage:
    olearyspicker.py [options]

Options:
    --longitude=long    Longitude value [default: 18.0388702]
    --latitude=lat      Latitude value [default: 59.3213309]
    --distance=dist     Distance in meters [default: 4000]
    -h, --help          Show this help and exit
    -v, --verbose       There is no verbose :(
"""

from __future__ import print_function, unicode_literals
import json
import random
import requests
from docopt import docopt


class restaurant(object):
    def __init__(self, title, short_title, slug, address, distance, phone, url):
        self.title = title
        self.short_title = short_title
        self.slug = slug
        self.address = address
        self.distance = distance
        self.phone = phone
        self.url = url


def banner(*text):
    longest = len(max(text, key=len))
    frame = '*' * (longest + 4)
    print(frame)
    for i, row in enumerate(text):
        print('{char} {text} {char}'.format(
            char='*',
            text=row.ljust(longest)))
    print(frame)


def main(args):
    r = requests.get("http://olearys.se/api/v1/restaurants/?language_code=sv-se&site_id=2&point={longitude},{latitude}&dist={distance}".format(**args))

    restaurants = []

    data = json.loads(r.text)
    if data['count'] >= 1:
        for line in json.loads(r.text)['results']:
            restaurants.append(restaurant(line['title'], line['short_title'], line['slug'], line['address'], line['distance'], line['phone'], line['url']))

        rest = restaurants[random.randrange(len(restaurants))]
        banner(rest.title, rest.address, rest.phone)

    else:
        banner("No restaurants found within that range and coordinates")


if __name__ == "__main__":
    args = docopt(__doc__, version='0.1.0-perhaps', help=True)
    args = {k[2:]: v for (k, v) in args.items()}
    main(args)
