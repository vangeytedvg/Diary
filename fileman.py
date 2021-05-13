from PyQt5.QtCore import QDir, QFile


class FileManager():
    """
      File operations on diary entries
    """

    @staticmethod
    def getfiles(path: str, year: int, month_nr: int):
        """
          Get the list of files for a given year-month 
        """
        month = str(month_nr) if month_nr > 9 else "0" + str(month_nr)
        pattern = str(year) + month + "*.html"
        manager = QDir()
        manager.setPath(path)
        manager.setNameFilters([pattern])
        files = manager.entryList()
        return files

    @staticmethod
    def page_exists(filename: str) -> bool:
        """
          Simply test if a diary page (file) exists
        """
        if QFile(filename).exists():
            return True
        return False

    @staticmethod
    def page_exists_(year: int, month_nr: int, day_nr: int) -> bool:
        """
          Test a date existance file
        """
        month = str(month_nr) if month_nr > 9 else "0" + str(month_nr)
        day = str(day_nr) if day_nr > 9 else "0" + str(day_nr)
        filename = str(year) + month + day + ".html"
        if QFile(filename).exists():
            return True
        return False

    @staticmethod
    def make_diary_filename(year: int, month_nr: int, day: int) -> int:
        month = str(month_nr) if month_nr > 9 else "0" + str(month_nr)
        day = str(day_nr) if day_nr > 9 else "0" + str(day_nr)
        return year + month + day + ".html"
