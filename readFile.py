import csv

class ReadFile:
    def __init__ (self, fileName):
        self.name = fileName
        self.headers = []
        self.information = dict()

    def readParser(self):
        with open(self.name, mode='r') as csvReadFile:
            readFile = csv.DictReader(csvReadFile)
            self.headers = [header.strip() for header in readFile.fieldnames]

            for line in readFile:
                for header in self.headers:
                    if line[header] != '' and 'State' not in header:
                        stateKey = int(line['ï»¿State'])
                        inputStringKey = header
                        self.information[(stateKey, inputStringKey)] = line[header]

    def readCFG(self):
        with open(self.name, mode='r') as csvReadFile:
            readFile = csv.DictReader(csvReadFile)
            self.headers = [header.strip() for header in readFile.fieldnames]

            for line in readFile:
                resultKey = line['ï»¿Result'].strip()
                equation = line['Equation']
                if resultKey in self.information:
                    self.information[resultKey].append(equation)
                else:
                    self.information[resultKey] = [equation]