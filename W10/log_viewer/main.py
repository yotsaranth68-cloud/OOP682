
from PySide6.QtWidgets import QApplication
from services.file_source import FileLogSource
from services.mock_source import MockLogSource
from ui.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication([])
    log = MockLogSource()
    log = FileLogSource("logs/voters.log")
    viewer = MainWindow(log)
    viewer.show()
    app.exec()
