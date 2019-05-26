import six

from abc import ABCMeta, abstractmethod, abstractstaticmethod


@six.add_metaclass(ABCMeta)
class Builder:
    """
    构建器
    """
    @abstractmethod
    def headers(self, options):
        pass

    @abstractmethod
    def params(self, params, options):
        pass

    def url(self, url, options):
        return url.format(**options)


@six.add_metaclass(ABCMeta)
class Requester:
    """
    请求器
    """
    @abstractmethod
    def __call__(self, method, url, headers, params):
        pass


@six.add_metaclass(ABCMeta)
class Responder:
    """
    响应处理器
    """
    def __init__(self):
        self._data = None

    def new(self, data):
        self._data = data
    
    @abstractmethod
    def parser(self):
        pass