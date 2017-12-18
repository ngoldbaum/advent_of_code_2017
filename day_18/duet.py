from collections import deque


class Computer:
    def __init__(self, registers, program):
        self.registers = registers
        self.program = program
        self.nlines = len(self.program)
        self.send_count = 0
        self.index = 0
        self.queue = deque([])
        self.out_queue = []

    def run_line(self, instruction, register, arg):
        offset = 1
        if isinstance(arg, str):
            arg = self.registers[arg]
        if instruction == 'set':
            self.registers[register] = arg
        elif instruction == 'add':
            self.registers[register] += arg
        elif instruction == 'mul':
            self.registers[register] *= arg
        elif instruction == 'mod':
            self.registers[register] %= arg
        elif instruction == 'snd':
            try:
                snd_val = int(register)
            except ValueError:
                snd_val = self.registers[register]
            self.out_queue.append(snd_val)
            self.send_count += 1
        elif instruction == 'rcv':
            self.registers[register] = self.queue.pop()
        elif instruction == 'jgz':
            try:
                cmp_val = int(register)
            except ValueError:
                cmp_val = self.registers[register]
            if cmp_val > 0:
                offset = arg
        else:
            raise RuntimeError
        return offset

    def run(self):
        while True:
            line = self.program[self.index]
            instruction = line[0]
            register = line[1]
            try:
                try:
                    arg = int(line[2])
                except ValueError:
                    arg = line[2]
            except IndexError:
                arg = None
            if instruction == 'rcv' and len(self.queue) == 0:
                break
            self.index += self.run_line(instruction, register, arg)
            if self.index < 0 or self.index > self.nlines:
                import pdb; pdb.set_trace()


if __name__ == "__main__":
    with open('input', 'r') as f:
        text = f.readlines()

    program = [t.strip().split(' ') for t in text]

    registers = set()
    for l in program:
        try:
            int(l[1])
        except ValueError:
            registers.add(l[1])

    registers = dict([(r, 0) for r in registers])
    r0 = registers.copy()
    r1 = registers.copy()
    r1['p'] = 1
    c0 = Computer(r0, program)
    c1 = Computer(r1, program)
    while True:
        c0.run()
        c1.run()
        for item in c0.out_queue:
            c1.queue.appendleft(item)
        c0.out_queue = []
        for item in c1.out_queue:
            c0.queue.appendleft(item)
        c1.out_queue = []
        if len(c0.queue) == 0 and len(c1.queue) == 0:
            break
    print(c1.send_count)
