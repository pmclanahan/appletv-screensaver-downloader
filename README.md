Download AppleTV screensaver videos
===================================

Get a local copy of those [sweet aerial videos](https://www.apple.com/tv/experience/#ig4) for use with the
[save hollywood screensaver](http://s.sudre.free.fr/Software/SaveHollywood/about.html) or the like.

Installation & Use
------------------

Clone this repo. Then run the following commands:

```bash
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ ./download.py
```

This will download the videos into the `videos` directory. If the URL for the videos data
were to change, you can pass in an alternate URL as an argument to `download.py`.

Enjoy!

\- pmac
