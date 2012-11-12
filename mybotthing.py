# coding: utf-8

import urllib2

import HTMLParser

class LinkFinder(HTMLParser.HTMLParser):
    def __init__(self, *args, **kwargs):
        HTMLParser.HTMLParser.__init__(self, *args, **kwargs)
        self.in_tweet = False
        self.tweets = []
    def handle_starttag(self, tag, attrs):
        if tag == "p" and dict(attrs)['class'] == "js-tweet-text": # found tweet
            self.in_tweet = True
            #self.tweets.append([dict(attrs)['p']])
    def handle_endtag(self, tag):
        if tag == "p" and self.in_tweet: # ignore '<a name=""...'
            self.in_tweet = False
    def handle_data(self, data):
        if self.in_tweet and data != "@":
            self.tweets.append(data)

def pullTweets():
    """pulls tweet archives and returns a list of strings"""
    req = urllib2.Request(u'http://localhost/%EF%BC%A4%EF%BC%B2%EF%BC%A1%EF%BC%A7%EF%BC%AF%EF%BC%AE%EF%BC%B3%EF%BC%AC%EF%BC%B5%EF%BC%B4%20(hentaiphd)%20on%20Twitter.html')
    anime = urllib2.urlopen(req).read()
    lf = LinkFinder()
    lf.feed(anime)
    lf.close()
    return lf.tweets

if __name__ == "__main__":

    newTweetList = pullTweets()

    for tweet in newTweetList:
        print tweet