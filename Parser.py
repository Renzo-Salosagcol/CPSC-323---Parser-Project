class LRParser:
    def __init__(self, parsing_table, cfg):
        self.parsing_table = parsing_table
        self.cfg = cfg
        self.stack = ['0']
        self.stackOrder = ['$0']
        self.actions = []

    def parse(self, input_string):
        pass
        # a = input_string[0]
        # while True:
        #     s = int(self.stack[-1])  # Current state
        #     action = self.parsing_table.get((s, a), None)
        #
        #     if action is None:
        #         self.actions.append(f'Error: Unrecognized symbol or state')
        #         return False, self.actions
        #
        #     self.actions.append(f'Stack: {self.stack}, Input: {input_string}, Action: {action}')
        #
        #     if action.startswith('s'):  # Shift
        #         self.stack.append(a)
        #         self.stack.append(action[1:])
        #         input_string = input_string[1:]
        #     elif action.startswith('r'):  # Reduce
        #         rule_idx = int(action[1:])
        #         lhs, rhs = self.cfg[rule_idx]
        #         for _ in range(2 * len(rhs)):
        #             self.stack.pop()
        #         s = int(self.stack[-1])
        #         self.stack.append(lhs)
        #         self.stack.append(str(self.parsing_table.get((s, lhs), None)))
        #     elif action == 'acc':
        #         self.actions.append(f'Stack: {self.stack}, Input: {input_string}, Action: {action}')
        #         return True, self.actions
        #
        #     if input_string:
        #         a = input_string[0]
        #     else:
        #         a = '$'

    def reset(self):
        self.stack = ['0']
        self.actions = []