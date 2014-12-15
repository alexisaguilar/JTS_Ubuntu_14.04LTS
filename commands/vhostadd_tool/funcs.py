#!/usr/bin/env python
# -*- coding: utf8 -*-

from os import system

from settings import APACHE_PATH, APACHE_RESTART_COMMAND


def _set_folder_tree(p, apptype):
    extra = "public" if apptype is 'py' else ""
    command = "/bin/bash %s/tree_generator.sh %s %s" % (_get_origen(), p, extra)
    system(command)
    _create_ini_file(p, apptype)
    print "Estructura de directorios creada:"
    system("tree /srv/websites/%s/" % p)
    system("chmod -R 755 /srv/websites/%s/" % p)
    print "·" * 60


def _create_ini_file(p, apptype):
    tmpl = 'controller.py' if apptype is 'py' else 'index.php'
    origen = _get_origen()
    target = "/srv/websites/%s/application/" % p
    command = "cp %s/templates/%s %s" % (origen, tmpl, target)
    system(command)


def _render_vhost(p, apptype='py'):
    origen = _get_origen()
    folder = "%s/templates" % origen
    file = "%s/vhost_%s" % (folder, apptype)
    with open(file, 'r') as base:
        return base.read().replace('SERVERNAME', p)


def _get_origen():
    dirs = __file__.split('/')
    return "/".join(dirs[0:len(dirs)-1])


def create_vhost(p, apptype='py'):
    _set_folder_tree(p, apptype)
    content = _render_vhost(p, apptype)

    file = "%s.conf" % p.split('.')[0]
    vhost_file = "%s/%s" % (APACHE_PATH, file)
    with open(vhost_file, 'w') as newvhost:
        newvhost.write(content)

    print "Habilitar nuevo VirtualHost:"
    command = "a2ensite %s; %s" % (file, APACHE_RESTART_COMMAND)
    system(command)
