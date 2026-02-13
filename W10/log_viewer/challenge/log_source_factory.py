from log_viewer.file_log_source import FileLogSource
from log_viewer.csv_log_source import CsvLogSource
import os

class LogSourceFactory:
    @staticmethod
    def create(filepath):
        _, ext = os.path.splitext(filepath)

        if ext == ".csv":
            return CsvLogSource(filepath)
        else:
            return FileLogSource(filepath)

