#! /usr/bin/env python3
import argparse
import hashlib


def create_parse():
    """ set up parser options """
    parser = argparse.ArgumentParser(description="file hashing utility")
    parser.add_argument("target", help="one or more files to be hashed", nargs="+")
    return parser


def Many_Hash(filename):
    """ calculate hashes for given filename """
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
    targets = args.target
    for target in targets:
        size, md5, sha1, sha256, sha512 = Many_Hash(target)
        print(
            "Name: {}\nSize: {:,}\nMD5: {}\nSHA1: {}\nSHA256: {}\nSHA512: {}\n".format(
                target, size, md5, sha1, sha256, sha512
            )
        )


if __name__ == "__main__":
    main()
