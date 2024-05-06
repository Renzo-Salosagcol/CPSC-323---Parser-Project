from readFile import ReadFile
from writeFile import create_results_file
from Parser import LRParser
def main():
    inputs = ["(id+id)*id$", "id*id$", "(id*)$"]

    # Read parsing table file
    parsingTable = ReadFile('ParsingTable.csv')
    parsingTable.readParser()

    # Read CFG file
    cfg = ReadFile('CFG.csv')
    cfg.readCFG()

    # print(parsingTable.information)
    # print(cfg.information)

    # Create an LR parser instance
    parser = LRParser(parsingTable.information, cfg.information)

    # Parse the given input strings
    results = {}
    firstIteration = True
    for input_str in inputs:
        parser.reset()
        accepted, actions = parser.parse(input_str)
        results[input_str] = {
            'accepted': accepted,
            'actions': actions
        }

        if firstIteration:
            create_results_file(input_str, parser, 'w')
            firstIteration = False
        else:
            create_results_file(input_str, parser, 'a')

if __name__ == '__main__':
    main()