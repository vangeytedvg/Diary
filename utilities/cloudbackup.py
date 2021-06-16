"""
Perform a backup to the Cloud.  For the moment there is only one subclass.
This subclass specializes in working with Google Drive
"""
import zipfile
import zlib
import os.path

from PyQt5.QtCore import QFile, QDir, QObject, pyqtSignal

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from apiclient.http import MediaFileUpload

from .dvgFileUtils import next_filename, extractFileNameOnly


class NoDiaryPagesFound(Exception):
    """
    Custom exception in case no content can be found in the given location.
    This exception is known directly in the main.py class.
    """

    def __init__(self, path, msg="No diary files in given location"):
        self.path = path
        self.message = msg

    def __str__(self):
        return f"{self.path} {self.message}"


class DiaryPagesDirectoryNotFound(Exception):
    """
    Custom exception in case no content can be found in the given location.
    This exception is known directly in the main.py class.
    """

    def __init__(self, path, msg="Provided diary folder not found"):
        self.path = path
        self.message = msg

    def __str__(self):
        return f"{self.path} {self.message}"


class GoogleDrive(QObject):
    def __init__(self, folder_id: str):
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

    def upload_file(self, filename: str, path: str):
        """ Load a new file or update an existing one """
        media = MediaFileUpload(f"{path}/{filename}")
        response = self.service.files().list(
            q=f"name='{filename}' and parents = '{self.__folder_id}'",
            spaces='drive',
            fields='nextPageToken, files(id, name)',
            pageToken=None).execute()

        if len(response['files']) == 0:
            # File was not found, so create a brand new file in the google drive
            file_metadata = {
                'name': filename,
                'parents': [self.__folder_id]
            }
            file = self.service.files().create(body=file_metadata, media_body=media, fields='id').execute()
            return file
        else:
            for myfile in response.get('files', []):
                # Process changed files
                update_file = self.service.files().update(
                    fileId=myfile.get('id'),
                    media_body=media, ).execute()

            return "Updated"

    def test_run(self, l: int):
        # Call the Drive v3 API
        results = self.service.files().list(
            pageSize=l,
            fields="nextPageToken, files(id, name)"
        ).execute()
        items = results.get('files', [])
        if not items:
            return "No items found"
        else:
            return items


class Backup(QObject):
    """
    Base class for backups
    """
    _zipname = ""
    _source_path = ""

    finished = pyqtSignal(str)

    def __init__(self, source_path: str):
        super().__init__()
        self._source_path = source_path

    def zip_diary(self):
        """
        Make a zipfile with the give name.  This method is for
        all instances the same.
        """
        file_list = QDir(self._source_path)
        file_list.setNameFilters(["*.html"])

        if not file_list.exists():
            raise DiaryPagesDirectoryNotFound

        # Start zipping if we have files
        if len(file_list) > 0:
            new_zip_name = next_filename(self._source_path, "bck_")
            self._zipname = extractFileNameOnly(new_zip_name)
            with zipfile.ZipFile(new_zip_name, "w") as my_zip:
                for file in file_list:
                    my_file = self._source_path + "/" + file
                    my_zip.write(my_file, compress_type=zipfile.ZIP_DEFLATED)
        else:
            raise NoDiaryPagesFound(self._source_path)

    def push_to_path(self):
        raise NotImplementedError("<pushtopath> must be overriden")

    def is_alive(self, l):
        raise NotImplementedError("<is_alive> must be overriden")


class LocalBackup(Backup):
    def __init__(self, zipname, source_path):
        super(LocalBackup, self).__init__(zipname, source_path)

    def push_to_path(self):
        print("Pushing to local")

    def is_alive(self, l: str):
        """
        Perform a simple connection test
        """
        my_test = []
        return my_test


class GoogleBackup(Backup):
    """
    Backup to google.
    """

    def __init__(self, source_path, folder_id):
        # folder_id is local to this class
        super(GoogleBackup, self).__init__(source_path)
        self.my_google_drive = GoogleDrive(folder_id)

    def push_to_path(self):
        """ Perform the actual backup """
        result = self.my_google_drive.upload_file(self._zipname,
                                                  self._source_path)
        self.finished.emit(self._zipname)
        return self._zipname

    def is_alive(self, l: str):
        """
        Perform a simple connection test
        """
        my_test = self.my_google_drive.test_run(l)
        return my_test
