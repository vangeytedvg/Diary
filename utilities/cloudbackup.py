"""
Perform a backup to the Cloud.  For the moment there is only one subclass.
This subclass specializes in working with Google Drive
"""
import zipfile

import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


class GoogleDrive():
    def __init__(self):
        # If modifying these scopes, delete the file token.json.
        SCOPES = ['https://www.googleapis.com/auth/drive']

        """
        Shows basic usage of the Drive v3 API.
        Prints the names and ids of the first 10 files the user has access to.
        """
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        self.service = build('drive', 'v3', credentials=creds)

    def test_run(self, l):
        # Call the Drive v3 API
        results = self.service.files().list(
            pageSize=l, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])
        if not items:
            return("No items found")
        else:
            return items


class Backup():
    def __init__(self, zipname):
        self.zipname = zipname
        pass

    def backup(self):
        pass

    def zip_file(self):
        pass


class CloudBackup(Backup):
    """
    Base class for cloud backups
    """
    _zipname = ""

    def __init__(self, zipname):
        super(CloudBackup, self).__init__(zipname)
        pass

    def backup(self):
        """
        Do work preparation
        """
        print("Zipping files")
        self.zipfile()

    def zipfile(self):
        print("Zipped " + self._zipname)


class GoogleBackup(CloudBackup):
    """
    Backup to google
    """

    def __init__(self, zipname):
        super(GoogleBackup, self).__init__(zipname)
        self.my_google_drive = GoogleDrive()

    def backup(self):
        super(GoogleBackup, self).backup()

    def push_to_google(self):
        print("Bye bye from " + self._zipname)

    def is_google_alive(self, l):
        """
        Perform a simple connection test
        """
        my_test = self.my_google_drive.test_run(l)
        return my_test
