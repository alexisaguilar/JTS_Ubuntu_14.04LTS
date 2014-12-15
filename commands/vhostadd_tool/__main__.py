#!/usr/bin/env python
# -*- coding: utf8 -*-

from sys import path
path.append(__file__.replace('/__main__.py', ''))
from argparse import ArgumentParser

from funcs import create_vhost


argp = ArgumentParser(
    prog='vhostadd',
    version='1.0',
    description='Agrega un nuevo VirtualHost a Apache',
    epilog='(C) Copyright 2014 Eugenia Bahit - GPL v3.0'
)

argp.add_argument('-s', '--server-name', dest='host', type=str, required=True,
    default=None, help='Nombre del dominio (example.org)')

argp.add_argument('-l', '--language', dest='lang',
    choices=['php', 'python'], default='php', type=str, required=False,
    help='Módulo con el que deberá interpretarse')

args = argp.parse_args()


apptype = 'py' if args.lang == 'python' else 'php'
create_vhost(args.host, apptype)
