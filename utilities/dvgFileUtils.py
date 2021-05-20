"""
    Filename and other utilities
    Author        : Danny Van Geyte
    Created       : March 2019
    Last Modified : May 2021
"""
import os
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMessageBox
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


def str_to_bool(comp):
    """
    Simple trick to convert string values to boolean
    return : True or False
    """
    if comp == True or comp == False:
        return comp
    return comp.lower() in ("true", "TRUE", "True", "yes", "Yes", "YES")


def extractFileNameOnly(filepath):
    """
    return the filename of the given path
    """
    head, tail = os.path.split(filepath)
    return tail


def extractPathOnly(filepath):
    """
    Return the path 
    """
    head, tail = os.path.split(filepath)
    return head


def extractExtension(filepath):
    """
    Return the extension of the given path
    """
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
        '_' + dateString + "_{:03d}.zip"
    n = 1

    while True:
        result = pattern.format(n)
        if not os.path.exists(result):
            return result
        n = n + 1


def nukeFile(filename):
    """
    Remove a file
    """
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


def ask(title="No Title", msg="No Message", explain="No explanation"):
    """
    Question messagebox
    """
    msgBox = QMessageBox()
    msgBox.setWindowTitle(title)
    msgBox.setText(msg)
    msgBox.setInformativeText(explain)
    msgBox.setIcon(QMessageBox.Question)
    msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msgBox.setDefaultButton(QMessageBox.Cancel)
    return msgBox.exec_()


def warn(parent, title="No Title", msg="No Message", explain="No explanation"):
    reply = QMessageBox.warning(parent, msg, explain, QMessageBox.Ok)


def info(parent, title="No Title", msg="No Message", explain="No explanation"):
    reply = QMessageBox.information(parent, msg, explain, QMessageBox.Ok)

