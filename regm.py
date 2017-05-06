import sys

def interpet_line(registers_contents, instruction):
    label, body = instruction.split(' : ')
    if body == 'HALT':
        return
    
    reg, labels = body.split(' -> ')
    reg_num = int(reg[1])
    reg_op = reg[2]
    labels = [label[1] for label in labels.split(', ')]

    if reg_op == '+':
        new_label = int(labels[0])
        registers_contents[reg_num] += 1

    elif reg_op == '-':
        if registers_contents[reg_num] > 0:
            new_label = int(labels[0])
            registers_contents[reg_num] -= 1
        else:
            new_label = int(labels[1])

    return new_label, registers_contents

def interpret(filename):
    with open(filename) as f:
        contents = f.read()
    lines = contents.split('\n')

    registers = None
    registers_contents = None
    instructions = None
    for i in range(len(lines)):
        if lines[i] == 'registers:':
            registers = lines[i + 1].split()
        if lines[i] == 'configuration:':
            registers_contents = map(int, lines[i + 1].split())
        if lines[i] == 'instructions:':
            instructions = lines[i + 1:]

    if registers is None or registers_contents is None or instructions is None:
        print 'Malformed program!'
        sys.exit(1)

    label = 0

    print ' '.join(['Li'] + registers)
    print

    while True:
        print '  '.join(map(str, [label] + registers_contents))
        configuration = interpet_line(registers_contents, instructions[label])
        if configuration is None:
            break
        label, registers_contents = configuration
    
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage: python main.py [input file]"
        sys.exit(1)
    input_file = sys.argv[1]

    interpret(input_file)
