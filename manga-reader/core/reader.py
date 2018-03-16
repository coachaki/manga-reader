import sys
import argparse
import zipfile

parser = argparse.ArgumentParser(description="Read manga")
parser.add_argument("path", nargs="?",  help="path help")

args = parser.parse_args()


class Reader(object):
    pass


def open_volume(path):
    print(path)
    if zipfile.is_zipfile(path):
        print("yes")
        myzip = zipfile.ZipFile(path)
        print(myzip.namelist())
    else:
        print("no")


if __name__ == '__main__':
    open_volume(args.path)