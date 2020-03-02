#! /usr/bin/env python3
import argparse
import datetime
import os
import random
import sys
import hashlib

def create_parse():
    """ set up parser options """
    parser = argparse.ArgumentParser(description="file hashing shell extension")
    parser.add_argument("target", help="file to be hashed")
    return parser


def Many_Hash(filename):
    """ calculate hashes for given filename """
    print("Hashing {}".format(filename))
    with open(filename, "rb") as f:
#    with open(filename) as f:
        data = f.read()
#    data = data.encode("UTF-8")
    md5 = hashlib.md5(data).hexdigest()
#    print("MD5: {}".format(md5)) 
    sha1 = hashlib.sha1(data).hexdigest()
#    print("SHA1: {}".format(sha1)) 
    sha256 = hashlib.sha256(data).hexdigest()
#    print("SHA256: {}".format(sha256))
    sha512 = hashlib.sha512(data).hexdigest()
#    print("SHA512: {}".format(sha512)) 
    return len(data), md5, sha1, sha256, sha512


def main():
    """ main event loop """
    parser = create_parse()
    args = parser.parse_args()
    target = args.target
    size, md5, sha1, sha256, sha512 = Many_Hash(target)
    print("MD5: {}\nSHA1: {}\nSHA256: {}\nSHA512: {}".format(md5, sha1, sha256, sha512))

if __name__ == "__main__":
    main()
