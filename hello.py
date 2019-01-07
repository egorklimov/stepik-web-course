# -*- coding: utf-8 -*-
"""

Simple WSGI app for hw02 - https://stepik.org/lesson/14826/step/11

"""

def app(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    start_response(status, headers)
    return [(i + '\n') for i in environ['QUERY_STRING'].split('&')]