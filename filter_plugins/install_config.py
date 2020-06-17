#!/usr/bin/python

from __future__ import absolute_import, division, print_function

import json


def remove_auth(config):
    try:
        pullSecret = json.loads(config['pullSecret'])
        for data in pullSecret.get('auths', {}).values():
            data['email'] = 'secret@example.com'
            data['auth'] = 'secret'

        config['pullSecret'] = json.dumps(pullSecret)
    except KeyError:
        pass

    try:
        hosts = config['platform']['baremetal']['hosts']
        for host in hosts:
            host['bmc']['username'] = 'secret'
            host['bmc']['password'] = 'secret'
    except KeyError:
        pass

    return config


class FilterModule(object):
    def filters(self):
        return {
            'remove_auth': remove_auth,
        }
