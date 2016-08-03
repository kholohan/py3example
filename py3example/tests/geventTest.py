import logging

import py3example.parallelism.gevent as gevent

logging.basicConfig(level=logging.DEBUG)

gevent.searchTwitter("Potato", "Machine Learning", "Networking", "Computer Science")