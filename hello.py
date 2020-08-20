def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    answer = bytes('\r\n'.join(environ['QUERY_STRING'].split('&')), encoding="utf8")
    return [answer]
