# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from os.path import exists, expanduser, join

setting_file = join(expanduser('~'), '.mcmrc')
settings = {}

if exists(setting_file):
    with open(setting_file) as f:
        lines = f.readlines()
        for line in lines:
            if '=' in lines:
                key, value = line.split('=', 1)
                settings[key] = value