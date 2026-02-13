class Machine:
    def print(self, document):
        pass
    def scan(self, document):   
        pass
    def fax(self, document):
        pass
class OldPrinter(Machine):
    def print(self, document):
        print("Printing document...")
    def scan(self, document):
        raise NotImplementedError("This printer cannot scan")
    def fax(self, document):
        raise NotImplementedError("This printer cannot fax")