from copy import deepcopy

class HandHeld:
    
    def __init__(self):
        self.acc = 0
        self.pos = 0
        self.prev = 0
        self.size = 0
    
    def run(self, code):
        self.size = len(code)
        executed = set()
        
        while self.pos not in executed:
            executed.add(self.pos)
            self.execute(code[self.pos])
        
        return self.acc
    
    def reset(self):
        self.acc = 0
        self.pos = 0
        self.prev = 0
        self.size = 0

    # Not so elegant Bruteforce.
    def repaired_run(self, code):
        for i, command in enumerate(code):
            changed = deepcopy(code)
            if command.startswith('jmp'):
                changed[i] = command.replace('jmp', 'nop')
            elif command.startswith('nop'):
                changed[i] = command.replace('nop', 'jmp')
            else:
                continue
            out = self.run(changed)
            if self.prev == self.size - 1 and self.pos == 0:    
                return out
            else:
                self.reset()

    def execute(self, command):
        command, arg = command.split()
        
        self.prev = int(self.pos)
        if command == 'jmp':
            self.pos += int(arg)
        else:
            self.acc += int(arg)*(command=='acc')
            self.pos += 1
        self.pos %= self.size
        