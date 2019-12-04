def get_input():
    return list(map(int, open("day2_input.txt", "r").read().split(','))) 


class Computer:
    def __init__(self, tape):
        self._pos = 0 
        self._tape = tape 
        self._op_code_map = {}

    @property
    def tape(self):
        return self._tape

    @tape.setter
    def tape(self, val):
        self._tape = val
        self._pos = 0

    def add_opcode(self, code, jump, func): 
        """
        @param 
        func: func(tape, pos) 
        """
        self._op_code_map[code] = (jump, func) 

    def next(self):
        op_code = self._tape[self._pos] 
        jump, func = self._op_code_map[op_code]
        if not func(self._tape, self._pos):
            return False 
        self._pos += jump 
        return True 


def op_code_1(tape, pos):
    tape[tape[pos+3]] = tape[tape[pos+1]] + tape[tape[pos+2]] 
    return True


def op_code_2(tape, pos):
    tape[tape[pos+3]] = tape[tape[pos+1]] * tape[tape[pos+2]] 
    return True


def op_code_99(tape, pos):
    return False 


def run_comp(computer):
    while computer.next():
        pass


tape_ = get_input()
back_up_tape = list(tape_)
tape_[1] = 12
tape_[2] = 2 
compute = Computer(tape_) 
compute.add_opcode(1, 4, op_code_1)
compute.add_opcode(2, 4, op_code_2) 
compute.add_opcode(99, None, op_code_99) 

# Part 2
val_ = 19690720
for noun in range(100):
    for verb in range(100):
        tape_ = list(back_up_tape)
        tape_[1], tape_[2] = noun, verb
        compute.tape = tape_
        run_comp(compute)
        print(compute.tape[0])
        if compute.tape[0] == val_:
            print("FOUND ANSWER")
            print((100 * noun) + verb)
            exit(0)

exit(1)
while compute.next():
    print(compute._pos)

pos, tape = compute._pos, compute.tape 
print(tape[pos], tape[pos-1], tape[pos+1]) 
print(tape)
