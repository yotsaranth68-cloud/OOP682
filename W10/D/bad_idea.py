class MySQLDatabase:
    def query(self):
        print("Query MySQL")

class App:
    def __init__(self):
        self.db = MySQLDatabase()

    def get_data(self):
        self.db.query()
