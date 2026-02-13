
from PySide6.QtWidgets import QApplication
from services.mock_source import MockLogSource
from ui.main_window import MainWindow
from challenge.csv_source import CsvLogSource


if __name__ == "__main__":
    app = QApplication([])
    # Example: use the CSV source that implements ILogSource
    log = CsvLogSource("logs/voters.csv")
    viewer = MainWindow(log)
    viewer.show()
    app.exec()
