#!/usr/bin/env python
import json
import random
import requests


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
    distance = "4000"
    point = "18.0388702%2C59.3213309"
    r = requests.get("http://olearys.se/api/v1/restaurants/?language_code=sv-se&site_id=2&point={point}&dist={dist}".format(point=point, dist=distance))

    restaurants = []

    for line in json.loads(r.text)['results']:
        restaurants.append(restaurant(line['title'], line['short_title'], line['slug'], line['address'], line['distance'], line['phone'], line['url']))

    rand_rest = restaurants[random.randrange(len(restaurants))]

    print rand_rest.title
    print rand_rest.address
    print rand_rest.phone


if __name__ == "__main__":
    main()
