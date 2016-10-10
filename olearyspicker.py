#!/usr/bin/env python
import json
import random
import requests
import argparse


class restaurant(object):
    def __init__(
        self, title, short_title, slug, address, distance, phone, url):
        self.title = title
        self.short_title = short_title
        self.slug = slug
        self.address = address
        self.distance = distance
        self.phone = phone
        self.url = url


def main():
    parser = argparse.ArgumentParser(
        description="Find and randomize nearby O'learys restaurants. \
                     Stockholm central coordinates is 18.0686,59.3293. \
                     Gothenburg central is 11.9746,57.7089"
    )
    parser.add_argument('-d', '--distance',
                        type=int, default='4000',
                        help='Integer for distance in meters'
                        )
    parser.add_argument(
        '-c', '--coordinates',
        default='18.0686,59.3293',
        help='Coordinates in format {format} (W/E, N/S)'.format(
            format='18.0388702,59.3213309')
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
    
    api = "http://olearys.se/api/v1/restaurants/?language_code=sv-se&site_id=2"
    r = requests.get("{api}&point={coordinates}&dist={dist}".format(
        api=api, coordinates=coordinates, dist=distance))

    restaurants = []

    data = json.loads(r.text)
    if data['count'] >= 1:
        for line in json.loads(r.text)['results']:
            restaurants.append(restaurant(
                line['title'], line['short_title'], line['slug'],
                line['address'], line['distance'], line['phone'], line['url']))

        rand_rest = restaurants[random.randrange(len(restaurants))]

        print(rand_rest.title)
        print(rand_rest.address)
        print(rand_rest.phone)
    else:
        print("No restaurants found within that range and coordinates")
        print(args)


if __name__ == "__main__":
    main()
