class PDFReportGenerator:
    def __init__(self, data):
        self.data = data
    def generate(self):
        pass

class ExcelReportGenerator:
    def __init__(self, data):
        self.data = data
    def generate(self):
        pass

class EmailSender:
    def __init__(self, recipient):
        self.recipient = recipient
    def send(self, report):
        pass

   