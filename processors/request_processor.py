class RequestProcessor:
    """
    请求处理器
    """
    def __init__(self, builder, requester, responder):
        self._builder = builder
        self._requester = requester
        self._responder = responder

    def __call__(self, method, url, params, options, url_options=None):
        """
        构建头部 -> 构建请求参数 -> 请求 -> 解析请求
        """
        if url_options:
            url = self._builder.url(url, url_options)

        headers = self._builder.headers(options)
        params = self._builder.params(params, options)

        responses = self._requester(method, url, headers, params)
        self._responder.new(responses)
        
        return self._responder.parser()
