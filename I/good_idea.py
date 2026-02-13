from abc import abstractmethod

class Printer:
    @abstractmethod
    def print(self, document):
        pass
class Scanner:
    @abstractmethod
    def scan(self, document):
        pass
class Fax:
    @abstractmethod
    def fax(self, document):
        pass
class MultiFunctionDevice(Printer, Scanner, Fax):
    def print(self, document):
        print("Printing document...")
    def scan(self, document):
        print("Scanning document...")
    def fax(self, document):
        print("Faxing document...")