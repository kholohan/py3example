
import logging

import gevent

geventLogger = logging.getLogger("gevent")

#gevent is a coroutine-based Python networking library.
def retrieveTask(*args, **kwargs):
    searchTerm = args[0]
    if(searchTerm is not None):
        geventLogger.info("Initializing a twitter search for the following term: " + searchTerm)
    else:
        geventLogger.warn("Search term is non-existant, unable to query twitter")

def searchTwitter(*args, **kwargs):
    geventLogger.info("Search initialized for " + str(args) + ".")
    jobs = [gevent.spawn(retrieveTask, arg,) for arg in args]
    geventLogger.info(str(jobs.__len__()) + " jobs created.")
    gevent.joinall(jobs)

