import logging

import requests

from requests.exceptions import HTTPError

restLogger = logging.getLogger("rest")

class Rest(object):



    def __init__(self, endpoint, *args, **kwargs):
        self._endpoint = endpoint
        self._timeout = 10000
        self._headers = None
        self._auth = None

    def _createUrl(self, path, args):

    def _getSession(self):
        if self._session is None:
            requestsSession = requests.Session()
            # Add authentication here

    def _restGetOperation(self, url, returnedClass):
    	try:
            response = self._session.get(url, auth = self._auth, headers=self._headers, timeout=self._timeout)
        except requests.exceptions.Timeout as e:
            restLogger.warn("Request for " + url + " exceeded " + self._timeout)
        CoreSession._raise_for_status(response)
        returnedObject = self._decodeJson(response.text)
        if returnedClass is not None:
            if not isinstance(returnedObject, returnedClass):
                raise Exception("Expected {0} type but found {1}".format(returnedClass.__name__, returnedObject.__class__.__name__))
        return returnedObject

    def _raise_for_status(response):
        try:
            response.raise_for_status()
        except HTTPError as original_error:


    def get(self, path, *args):
        url = self._createUrl(path=path, args=args)
