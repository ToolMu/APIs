from processors.base import Builder


class HttporgBuilder(Builder):
    """
    https://httpbin.org/get
    """
    def headers(self, options):
        if options.get('user-agent'):
            options['user-agent'] = "OKHttp/8.8"
        return options

    def params(self, params, options):
        return params
