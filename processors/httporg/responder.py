from processors.base import Responder


class HttporgResponder(Responder):
    def parser(self):
        return self._data
