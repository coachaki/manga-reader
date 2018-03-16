import zipfile

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