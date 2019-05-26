import requests

from processors.base import Requester


class HttporgRequester(Requester):
    def __call__(self, method, url, headers, params):
        request_function = {
            "GET": self._get,
            "POST": self._post,
            "DELETE": self._delete,
            "PUT": self._put,
            "PATCH": self._patch
        }
        return request_function[method.upper()](url, headers, params)
    
    def _get(self, url, headers, params):
        return requests.get(url, headers=headers, params=params)

    def _post(self, url, headers, params):
        return requests.post(url, headers=headers, params=params)
    
    def _delete(self, url, headers, params):
        return requests.delete(url, headers=headers, params=params)

    def _put(self, url, headers, params):
        return requests.put(url, headers=headers, params=params)
    
    def _patch(self, url, headers, params):
        return requests.patch(url, headers=headers, params=params)
