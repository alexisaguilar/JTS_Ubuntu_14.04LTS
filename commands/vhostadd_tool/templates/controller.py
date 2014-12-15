# -*- coding: utf8 -*-
from sys import path
path.append(__file__.replace('/controller.py', ''))


def application(environ, start_response):
    salida = "Hello <b>Python</b> World!"
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf8')])
    return salida
