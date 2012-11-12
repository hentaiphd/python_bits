# coding: utf-8

import twitter
from collections import defaultdict
import pdb
import time
import random
from lxml import etree
from StringIO import StringIO
import urllib2

from hentai_secret import *
from mybotthing import pullTweets


def get_booru():
    req = urllib2.Request('http://gelbooru.com/index.php?page=dapi&s=comment&q=index')
    anime = urllib2.urlopen(req).read()

    context = etree.iterparse(StringIO((anime)))
    for action, elem in context:
        if random.randint(1, 10) == 1:
            words = elem.get('body').split(' ')
            choice = ' '.join(random.sample(words, random.randint(1, 3)))
            return choice

def replace_booru(string, inserting):
    string = string.split(' ')
    inserting = inserting.split(' ')
    top = len(string) - len(inserting)
    if top < 1:
        return ' '.join(string)

    index = random.randint(0, top)

    i = 0
    for item in inserting:
        string[index + i] = item
        i += 1
    return ' '.join(string)

if __name__ == "__main__":
    api = twitter.Api(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token_key=ACCESS_TOKEN_KEY, access_token_secret=ACCESS_TOKEN_SECRET)
    
    statuses = pullTweets()

    store = defaultdict(list)
    for s in statuses:
        words = s.split(' ')
        for i,word in enumerate(words):
            if i < len(words) - 1:
                index = i + 1
                store[word].append(words[index])



    while True:
        word = random.choice(store.keys())
        status = word
        while len(status) < 55 and store[word]:
            word = random.choice(store[word])
            status += " %s" % (word,)

        status = status.replace('@', '')

        print status
        api.PostUpdate(status)

        time.sleep(10*60)
