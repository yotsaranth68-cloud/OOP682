from interfaces.data_source import ILogSource


class MockLogSource(ILogSource):
    def get_logs(self) -> list[str]:
        return [
            "2024-01-01 12:00:00 INFO Application started",
            "2024-01-01 12:05:00 ERROR An unexpected error occurred",
            "2024-01-01 12:10:00 WARN Low disk space",
        ]