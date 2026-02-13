from interfaces.data_source import ILogSource
import csv
from typing import List


class CsvLogSource(ILogSource):
    """Read logs from a CSV file and produce a list of string messages.

    Each CSV row is converted to a human-readable string. If the CSV
    has headers, each field is shown as "header: value" pairs.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_logs(self) -> List[str]:
        rows: List[str] = []
        try:
            with open(self.file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                headers = next(reader, None)
                for r in reader:
                    if headers:
                        row = ", ".join(f"{h}: {v}" for h, v in zip(headers, r))
                    else:
                        row = ", ".join(r)
                    rows.append(row)
        except FileNotFoundError:
            return [f"CSV file not found: {self.file_path}"]
        except Exception as e:
            return [f"Error reading CSV: {e}"]
        return rows
