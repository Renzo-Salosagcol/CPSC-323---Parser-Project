import csv

class WriteFile:
    def __init__ (self, fileName, fileHeaders, fileInformation):
        self.name = fileName
        self.headers = fileHeaders
        self.information = fileInformation

def writeFile(file):
    with open(file.name, mode='w', newline='') as csvwritefile:
        writer = csv.DictWriter(csvwritefile, fieldnames=file.headers)
        writer.writeheader()

        for input in file.information:
            writer.writerow({file.headers[0]: input})
