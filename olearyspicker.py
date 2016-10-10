#!/usr/bin/env python
import json
import random
import requests
import argparse


class restaurant(object):
    def __init__(self, title, short_title, slug, address, distance, phone, url):
        self.title = title
        self.short_title = short_title
        self.slug = slug
        self.address = address
        self.distance = distance
        self.phone = phone
        self.url = url


def main():
    argparser = argparse.ArgumentParser(description="O'learys Picker")
    argparser.add_argument('--longitude', action='store', default='18.0388702')
    argparser.add_argument('--latitude', action='store', default='59.3213309')
    argparser.add_argument('--range', action='store', default='4000')
    args = argparser.parse_args()
    
    distance = args.range
    point = "{lon}%2C{lat}".format(lon=args.longitude, lat=args.latitude)
    api = "http://olearys.se/api/v1/restaurants/?language_code=sv-se&site_id=2"
    endpoint = "{api}&point={point}&dist={dist}".format(
        api=api, point=point, dist=distance)
    r = requests.get(endpoint)
    
    restaurants = []
    for line in json.loads(r.text)['results']:
        restaurants.append(restaurant(
            line['title'], line['short_title'], line['slug'], line['address'],
            line['distance'], line['phone'], line['url']))

    rand_rest = restaurants[random.randrange(len(restaurants))]

    print rand_rest.title
    print rand_rest.address
    print rand_rest.phone


if __name__ == "__main__":
    main()
