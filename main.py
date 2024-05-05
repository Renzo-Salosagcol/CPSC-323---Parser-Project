from readFile import ReadFile
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
    for input_str in inputs:
        parser.reset()
        accepted, actions = parser.parse(input_str)
        results[input_str] = {
            'accepted': accepted,
            'actions': actions
        }
    print(results)

if __name__ == '__main__':
    main()