Compiler Simulation for Syntax Analysis

This project is developed as part of the coursework for CPSC 323. It includes a compiler simulation that traces input strings over the set {id, +, *, ), (} and ending with $. The program uses a provided CFG and parsing table to simulate a stack-based parsing process, outputting the stack operations and determining whether the strings are accepted based on the defined grammar.
Table of Contents

    Getting Started
    Prerequisites
    Running the Simulation
    Files Description
    Output
    Contributing
    License

Getting Started

To get a local copy up and running follow these simple steps.
Prerequisites

    Python 3.8 or later
    No external libraries are required

Running the Simulation

    Clone the repository:

    bash

git clone https://github.com/Renzo-Salosagcol/CPSC-323---Parser-Project.git

Navigate to the project directory:

bash

cd CPSC-323---Parser-Project

Run the main script:

bash

    python main.py

Files Description

    main.py: Entry point of the program. It initializes the parsing process.
    Parser.py: Implements the parsing logic based on the parsing table and CFG.
    readFile.py: Utility to read input strings from a file.
    writeFile.py: Utility to write the output results to a file.
    CFG.csv: Contains the Context-Free Grammar used for parsing.
    ParsingTable.csv: Contains the parsing table used by the parser to decide actions.
    result.txt: Example output file, including stack actions and acceptance results.

Output

The output is formatted as follows for each input string:

    Displays each action taken by the parser.
    Indicates whether the string is accepted or not based on the grammar.

Example output:

vbnet

Input: (id+id)*id$
Stack:
Step  Stack  Input  Action
...   ...    ...    ...
Output: String is accepted

Contributing

Feel free to fork this repository and submit pull requests. You can also open issues if you find bugs or have feature suggestions.

License

Distributed under the MIT License. See LICENSE for more information.

Authors

Martin Nguyen, Renzo Salosagcol, and Alberto Molina
