#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import random
import os
from flipurr.toot import *
from flipurr.flickr import *
from flipurr.quorum import *

mastodon_user_name = os.getenv('MASTODON_USER_NAME')
mastodon_password = os.getenv('MASTODON_PASSWORD')
user_secret_file = os.getenv('USER_SECRET_FILE')
app_secret_file = os.getenv('APP_SECRET_FILE')
flickr_api_key = os.getenv('FLICKR_API_KEY')
flickr_api_secret = os.getenv('FLICKR_API_SECRET')
quorum_api_base_url = os.getenv('QUORUM_API_BASE_URL')
quorum_group_id = os.getenv('QUORUM_GROUP_ID')
quorum_api_jwt = os.getenv('QUORUM_API_JWT')

toot = new_toot_client(mastodon_user_name, mastodon_password, user_secret_file, app_secret_file)
init_flickr_client(flickr_api_key, flickr_api_secret)

SHAPES = ["combo", "triangle", "rect", "ellipse", "circle", "rotatedrect", "beziers", "rotatedellipse", "polygon"]

full_name, photo = fetch_interesting_photo()

if full_name != '' and photo != None:
    photo_url = photo.getPhotoUrl()

    mode = random.randrange(0, 8)
    while mode == 6: # skip beziers
        mode = random.randrange(0, 8)

    count = random.randrange(100, 300)
    shape = SHAPES[mode]


    # put purr to your path
    output = "/tmp/output.jpg"
    cmd = "/usr/local/bin/purr -i {} -o {} -n {} -m {} -v".format(full_name, output, count, mode)
    print(cmd)

    print(os.popen(cmd).read())

    msg = "{} x {} ({})".format(shape, count, photo_url)
    new_purr_toot(toot, full_name, output, msg)
    trx = new_purr_post(quorum_api_base_url, quorum_api_jwt, quorum_group_id, msg, full_name, output)
    print("quorum trx: {}".format(trx))
