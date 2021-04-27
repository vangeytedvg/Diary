"""
    Filename  and other utilities
    Author : Danny Van Geyte
    Last Modified : March 2019
"""
import os
from PyQt5.QtCore import QDate
import zipfile
# Regular Expression
import re
import glob


def isMailOk(address):
    """
        Check if an email adres is correct
    :param address: email to check
    :return: true if adress os ok, otherwise false
    """
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if re.search(regex, address):
        return True
    else:
        return False


def extractFileNameOnly(filepath):
    head, tail = os.path.split(filepath)
    return tail


def extractPathOnly(filepath):
    head, tail = os.path.split(filepath)
    return head


def extractExtension(filepath):
    filename, file_extension = os.path.splitext(filepath)
    return file_extension


def next_filename(catalogLocation, imgPrefix):
    """
    Return a unique filename based on some settings.
    The calculation simple, the hile loop tests if a file already exists.  If
    a unique filename is found (using the n counter) this name is returned.
    :return: New unique image filename
    """
    dateString = QDate.currentDate().toString("yyyyMMdd")
    pattern = catalogLocation + "/" + imgPrefix + \
        '_' + dateString + "_{:03d}.html"
    n = 1

    while True:
        result = pattern.format(n)
        if not os.path.exists(result):
            return result
        n = n + 1


def nukeFile(filename):
    os.remove(filename)


def getnoteslist(location):
    """
        Get all pdf files in location
    :param location: path to pdfs
    :return:
    """
    images = []
    pattern = os.path.join(location, '*.pdf')
    images.extend(glob.glob(pattern))
    return images


def makezip(base_folder, zipname, mailid):
    """
        Create zip file, based on the base and mailid
    :param base_folder: Base path to the file
    :param zipname: name of the zipfile to create
    :param mailid: id of the email (becomes part of path to file)
    :return:
    """
    print("IN MAKEZIP")
    new_base = base_folder + os.sep + str(mailid) + os.sep
    makepdfs(new_base)

    new_zip_filename = base_folder + os.sep + str(mailid) + os.sep + zipname
    zipper = zipfile.ZipFile(new_zip_filename, "w", compression=zipfile.ZIP_DEFLATED)

    for q in _pdfs(new_base):
        print(q)
        zipper.write(q)
    zipper.close()
    return new_zip_filename
