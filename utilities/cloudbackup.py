"""
Perform a backup to the Cloud
"""
import zipfile


class CloudBackup():
    def __init__(self):
        pass

    def backup(self):
        """
        Do work preparation
        """
        print("Zipping files")


class GoogleBackup(CloudBackup):
    """
    Backup to google
    """

    def __init__(self):
        super(GoogleBackup, self).__init__()

    def backup(self):
        super(GoogleBackup, self).backup()
        print("Copying zipper")

