#!/usr/bin/env python

import sys

import requests


VIDEO_DEFS_URL = 'http://a1.phobos.apple.com/us/r1000/000/Features/atv/AutumnResources/videos/entries.json'


def get_video_urls(data):
    for group in data:
        for video in group['assets']:
            yield video['url']


def get_video_data(url):
    print 'getting videos data'
    return requests.get(url).json()


def get_video(url):
    filename = url.split('/')[-1]
    filename = 'videos/' + filename
    sys.stdout.write('downloading {}.'.format(filename))
    resp = requests.get(url, stream=True)
    count = 0
    with open(filename, 'wb') as fd:
        for chunk in resp.iter_content(2048):
            fd.write(chunk)
            if count % 1000 == 0:
                sys.stdout.write('.')
                sys.stdout.flush()

            count += 1

    print 'done'


if __name__ == '__main__':
    videos_url = sys.argv[1] if len(sys.argv) > 1 else VIDEO_DEFS_URL
    for url in get_video_urls(get_video_data(videos_url)):
        get_video(url)
