#! /usr/bin/env python3
import argparse
import datetime
import os
import random
import sys
import hashlib

import PySimpleGUI as sg

def create_parse():
    """ set up parser options """
    parser = argparse.ArgumentParser(description="file hashing shell extension")
    parser.add_argument("target", help="file to be hashed")
    return parser

def Many_Hash(filename):
    """ calculate hashes for given filename """
    print("Hashing {}".format(filename))
    with open(filename, "rb") as f:
        data = f.read()
    md5 = hashlib.md5(data).hexdigest()
    sha1 = hashlib.sha1(data).hexdigest()
    sha256 = hashlib.sha256(data).hexdigest()
    sha512 = hashlib.sha512(data).hexdigest()
    return len(data), md5, sha1, sha256, sha512

def main():
    """ main event loop """
    parser = create_parse()
    args = parser.parse_args()
    target = args.target
    size, md5, sha1, sha256, sha512 = Many_Hash(target)

    layout = [ [sg.Text(target)],
           [sg.Text('Size: '), sg.In('{:,}'.format(size), key='size')],
           [sg.Text('MD5: '), sg.In('{}'.format(md5), key='MD5')],
           [sg.Text('SHA1: '), sg.In('{}'.format(sha1), key='SHA1')],
           [sg.Text('SHA256: '), sg.In('{}'.format(sha256), key='SHA256')],
           [sg.Text('SHA512: '), sg.In('{}'.format(sha512), key='SHA512')],
           ]

    window = sg.Window('File hash', layout, return_keyboard_events=True, grab_anywhere=False, size=(500, 200))

    while True:
        event, values = window.read()

        if event is not None:
            size, md5, sha1, sha256, sha512 = Many_Hash(target)
            window['MD5'].update(md5)
            window['SHA1'].update(sha1)
        else:
            break


if __name__ == "__main__":
    main()
