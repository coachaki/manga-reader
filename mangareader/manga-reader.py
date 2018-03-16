import sys
import argparse

import core

parser = argparse.ArgumentParser(description="Read manga")
parser.add_argument("path", nargs="?",  help="path help")

args = parser.parse_args()

if __name__ == '__main__':
    reader.open_volume(args.path)