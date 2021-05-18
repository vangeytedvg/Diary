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
from apiclient.http import MediaFileUpload


class GoogleDrive():
    def __init__(self, folder_id):
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
        self.__folder_id = folder_id

    def upload_file(self, filename, path, folder_id):
        """ Load a new file or update an existing one """
        media = MediaFileUpload(f"{path}{filename}")
        response = self.service.files().list(
            q=f"name='{filename}' and parents = '{folder_id}'",
            spaces='drive',
            fields='nextPageToken, files(id, name)',
            pageToken=None).execute()

        return true

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
    """
    Base class for backups
    """
    _zipname = ""
    _source_path = ""

    def __init__(self, zipname, source_path):
        self._zipname = zipname
        self._source_path = source_path

    def zipfile(self, source_path, zipname):
        self.__zipname = zipname
        self.__source_path = source_path
        print("SOURCE PATH ", source_path)
        print("ZIPKEN ", zipname)

    def push_to_path(self):
        raise NotImplementedError("<pushtopath> must be overriden")

    def is_alive(self):
        raise NotImplementedError("<is_alive> must be overriden")


class LocalBackup(Backup):
    def __init__(self):
        pass

    def push_to_path(self):
        print("Pushing to local")

    def is_alive(self, l):
        """
        Perform a simple connection test
        """
        my_test = []
        return my_test


class GoogleBackup(Backup):
    """
    Backup to google
    """

    def __init__(self, zipname=zipname, source_path=source_path, folder_id=folder_id):
        super(GoogleBackup, self).__init__(zipname, source_path)
        self.my_google_drive = GoogleDrive(folder_id)

    def push_to_path(self):
        self.my_folder_id = folder_id
        result = self.my_google_drive.upload_file(self.__zipname, folder_id)

    def is_alive(self, l):
        """
        Perform a simple connection test
        """
        my_test = self.my_google_drive.test_run(l)
        return my_test

