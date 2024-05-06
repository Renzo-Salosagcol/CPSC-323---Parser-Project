class LRParser:
    def __init__(self, parsing_table, cfg):
        self.parsing_table = parsing_table
        self.cfg = cfg
        self.stack = [0]
        self.stackOrder = ['$0']
        self.inputOrder = []
        self.actionOrder = []

    def parse(self, input_string):
        input = self.organize_string(input_string)

        while True:
            newString = ''.join(input)
            self.inputOrder.append(newString)

            try:
                self.actionOrder.append(self.parsing_table.get((self.stack[-1], input[0])))
            except:
                self.actionOrder.append('Error: Unrecognized Action')
                return False, self.actionOrder

            action = self.action_response(str(self.actionOrder[-1]))

            if action == "Shift":
                newState = str((self.actionOrder[-1][1:]))
                newStackOrderInput = str(input[0]) + newState
                self.stackOrder.append(self.stackOrder[-1]+newStackOrderInput)
                if '10' in newStackOrderInput:
                    newState = '10'
                elif '11' in newStackOrderInput:
                    newState = '11'
                self.stack.append(int(newState))
                input = input[1:]
            elif action == "Reduce":
                changedStackInput = self.stackOrder[-1]
                reduceIndex = int((self.actionOrder[-1])[-1])

                cfgResult = self.cfg.get(reduceIndex)[0]
                cfgEquation = self.organize_string(self.cfg.get(reduceIndex)[1])

                # Check for reduction equation match
                charCheck = 0
                for i in cfgEquation:
                    if i in changedStackInput:
                        charCheck += 1

                if charCheck != len(cfgEquation):
                    self.actionOrder.append('Error: Reduction Equation Mismatch')
                    return False, self.actionOrder

                for i in range(len(cfgEquation)):
                    self.stack.pop()
                    if 'id' == cfgEquation[0] or '10' in changedStackInput or '11' in changedStackInput:
                        changedStackInput = changedStackInput[:-3]
                    else:
                        changedStackInput = changedStackInput[:-2]

                changedStackInput += cfgResult + self.parsing_table.get((self.stack[-1], cfgResult))
                self.stackOrder.append(changedStackInput)

                if changedStackInput[-2] == '1' and changedStackInput [-1] == '0':
                    self.stack.append(10)
                elif changedStackInput[-2] == '1' and changedStackInput [-1] == '1':
                    self.stack.append(11)
                else:
                    self.stack.append(int(changedStackInput[-1]))
            elif action == "Accept":
                self.actionOrder.append("Parser Completed: Input Accepted!")
                self.print_information()
                return True, self.actionOrder
            else:
                self.actionOrder.append('Error: Unrecognized Action')
                self.print_information()
                return False, self.actionOrder

    def reset(self):
        self.stack = [0]
        self.stackOrder = ['$0']
        self.inputOrder = []
        self.actionOrder = []


    def organize_string(self, input_string):
            result = []
            for index in range(len(input_string)):
                if input_string[index] == 'i' and input_string[index + 1] == 'd':
                    result.append('id')
                elif input_string[index] == 'd':
                    pass
                else:
                    result.append(input_string[index])
            return result

    def action_response(self, action):
        if action[0] == 'S' or action[0] == 's':
            return "Shift"
        elif action[0] == 'R' or action[0] == 'r':
            return "Reduce"
        elif action == "accept" or action == "Accept":
            return "Accept"
        else:
            return "Unaccepted"

    def print_information(self):
        print("Stack: ", self.stack)
        print("Stack Order: ", self.stackOrder)
        print("Action Order: ", self.actionOrder)
        print("Input Order: ", self.inputOrder)
