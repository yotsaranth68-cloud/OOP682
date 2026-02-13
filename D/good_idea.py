from abc import ABC, abstractmethod

class DataSource(ABC):
    @abstractmethod
    def query(self):
        pass

class MySQLDatabase(DataSource):
    def query(self):
        print("Query MySQL")

class PostgresDatabase(DataSource):
    def query(self):
        print("Query PostgreSQL")

class App:
    def __init__(self, db: DataSource):
        self.db = db

    def get_data(self):
        self.db.query()

app = App(MySQLDatabase())
app = App(PostgresDatabase())
