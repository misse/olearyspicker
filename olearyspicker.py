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


def banner(*text):
    longest = len(max(text, key=len))
    frame = '*' * (longest + 4)
    print(frame)
    for i, row in enumerate(text):
        print('{char} {text} {char}'.format(
            char='*',
            text=row.ljust(longest).encode('utf-8')))
    print(frame)


def main():
    parser = argparse.ArgumentParser(
        description="Find and randomize nearby O'learys restaurants. Stockholm central coordinates is 18.0686,59.3293. Gothenburg central is 11.9746,57.7089, I hate argparse formatting"
    )
    parser.add_argument('-d', '--distance',
                        type=int, default='4000',
                        help='Integer for distance in meters'
                        )
    parser.add_argument('-c', '--coordinates',
                        default='18.0686,59.3293',
                        help='Coordinates in format {format} (W/E, N/S)'.format(format='18.0388702,59.3213309')
                        )
    args = parser.parse_args()

    if args.distance is not None:
        distance = args.distance
    else:
        distance = '4000'

    if args.coordinates is not None:
        coordinates = args.coordinates
    else:
        coordinates = '18.0388702,59.3213309'

    r = requests.get(
        "http://olearys.se/api/v1/restaurants/?language_code=sv-se&site_id=2&point={coordinates}&dist={dist}".format(coordinates=coordinates, dist=distance))

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
    main()
