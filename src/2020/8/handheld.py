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

    # Not so elegant Bruteforce.
    def repaired_run(self, code):
        for i, command in enumerate(code):
            alt = deepcopy(code)
            alt[i] = (command.replace('jmp', 'nop') if command.startswith('jmp')
                                            else command.replace('nop', 'jmp'))
            out = self.run(alt)
            
            if self.prev == self.size - 1 and self.pos == 0:    
                return out
            else:
                self.__init__()

    def execute(self, command):
        command, arg = command.split()
        
        self.prev = int(self.pos)
        if command == 'jmp':
            self.pos += int(arg)
        else:
            self.acc += int(arg)*(command=='acc')
            self.pos += 1
        self.pos %= self.size
        