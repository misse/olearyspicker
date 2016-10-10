#!/usr/bin/env python
from urllib2 import Request, urlopen, URLError
import json
import random

class restaurant(object):
    def __init__(self, title, short_title, slug, address, distance, phone, url):
        self.title = title
        self.short_title = short_title
        self.slug = slug
        self.address = address
        self.distance = distance
        self.phone = phone
        self.url = url

distance = "4000"
point = "18.0388702%2C59.3213309"
url = "http://olearys.se/api/v1/restaurants/?language_code=sv-se&site_id=2&point={0}&dist={1}".format(point, distance)
request = Request(url)

response = urlopen(request)

restaurants = []

data = json.loads(response.read())
for line in data['results']:
    restaurants.append(restaurant(line['title'], line['short_title'], line['slug'], line['address'], line['distance'],line['phone'], line['url']))

rand_rest = restaurants[random.randrange(len(restaurants))]

#print rand_rest.title
print rand_rest.address
print rand_rest.phone
