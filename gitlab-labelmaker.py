#!/usr/bin/env python3

import contextlib
import sys
import json
import yaml
import urllib.parse
import urllib.request

config = yaml.safe_load(open('.labelmaker_config.json'))
labelFile = yaml.safe_load(open(config['labelfile']))

repo = urllib.parse.quote_plus(config['user'] + '/' + config['repo'])

repoUrl = config['url'] + config['repoprefix'] + '/' + repo
url = repoUrl + '/labels'

if (len(sys.argv) == 2) and (sys.argv[1] == 'delete'):
    req = urllib.request.Request(url)
    req.add_header('PRIVATE-TOKEN', config['token'])

    with contextlib.closing(urllib.request.urlopen(req)) as res:
        labels = yaml.safe_load(res.read())

        for label in labels:
            delUrl = url + '?name=' + urllib.parse.quote_plus(label['name'])
            req = urllib.request.Request(delUrl, method='DELETE')
            req.add_header('PRIVATE-TOKEN', config['token'])
            with contextlib.closing(urllib.request.urlopen(req)) as delRes:
                delRes.read()

for label in labelFile:
    data = urllib.parse.urlencode(label).encode('utf-8')
    req = urllib.request.Request(url, data)
    req.add_header('PRIVATE-TOKEN', config['token'])

    try:
        with contextlib.closing(urllib.request.urlopen(req)) as res:
            res.read()
    except urllib.error.HTTPError as err:
        if err.code != 409:
            print("Something happened! Error code", err.code)
