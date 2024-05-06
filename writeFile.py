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

def create_results_file(input_str, parser, mode):
    with open(f"result.txt", f'{mode}') as output_file:
        numLines = 50
        padding = 15

        output_file.write(f'Input: {input_str}\nStack: \n{"-" * numLines}\n')
        output_file.write(f'Step{" " * (padding - 4)}Stack{" " * (padding - 5)}')
        output_file.write(f'Input{" " * (padding - 5)}Action{" " * (padding - 6)}\n')

        for i in range(len(parser.stackOrder)):
            stackStep = parser.stackOrder[i]
            inputStep = parser.inputOrder[i]
            actionStep = parser.actionOrder[i]

            if actionStep == None:
                actionStep = "None"

            # Step and Stack print on file
            output_file.write(f'{i + 1}{" " * (padding - len(str(i + 1)))}{stackStep}{" " * (padding - len(stackStep))}')

            # Print Input on file
            output_file.write(f'{inputStep}{" " * (padding - len(inputStep))}')

            # Print Action on file
            output_file.write(f'{actionStep}{" " * (padding - len(actionStep))}\n')

        output_file.write(f'{"-" * numLines}\n')

        if parser.actionOrder[-2] == "accept" or parser.actionOrder[-2] == "Accept":
            output_file.write(f'Parsing Successful!\n{parser.actionOrder[-1]}\n\n')
        else:
            output_file.write(f'Parsing Incomplete\n{parser.actionOrder[-1]} \n \n')
