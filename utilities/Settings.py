"""
    Description : SettingsManager
    Author      : danny
    File        : Settings.py
    Date        : 24/02/18
"""
from PyQt5.QtCore import QSettings, QPoint, QSize


class SettingsManager:
    """
        Handles the saving and loading of settings.  This class
        is as generic as it can be.
    """
    _owner = None
    _company = ""
    _section = ""

    def load_settings(self, my_settings, company, section):
        """
            Load the required parameter
        :param my_settings:
        :param section:
        :param company:
        :param my_setting: Name of setting
        :return: Value of setting
        """
        settings = QSettings(company, section)
        for setting in my_settings:
            my_settings[setting] = settings.value(setting, "Nothing")
        return my_settings

    def saveSettings(self, my_settings, company, section):
        """
            Write Settings
        :param my_settings: Dict with setting key and values
        :param company:
        :param section:
        :return:
        """
        settings = QSettings(company, section)

        for setting in my_settings:
            settings.setValue(setting, my_settings[setting])