import csv
from log_viewer.log_source import ILogSource

class CsvLogSource(ILogSource):
    def __init__(self, filepath):
        self.filepath = filepath

    def read_logs(self):
        logs = []
        with open(self.filepath, newline='', encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                logs.append(" | ".join(row))
        return logs
