
def encode_pair1(x, y):
    return 2 ** x * (2 * y + 1)

def encode_pair2(x, y):
    return encode_pair1(x, y) - 1

def encode_list(xs):
    if xs == []:
        return 0
    else:
        return encode_pair1(xs[0], encode_list(xs[1:]))

def encode_instruction(instruction):
    if instruction == 'HALT':
        return 0
    if instruction[2] == '+':
        i = int(instruction[1])
        j = int(instruction[-1])
        return encode_pair1(2 * i, j)
    if instruction[2] == '-':
        i = int(instruction[1])
        j = int(instruction[-5])
        k = int(instruction[-1])
        return encode_pair1(2 * i + 1, encode_pair2(j, k))

def encode_program(program):
    return encode_list(map(encode_instruction, program))


def decode_pair_helper(n, c):
    b = bin(n)
    x = 0
    while b[-1] == c:
        b = b[:-1]
        x += 1
    y = int(b[:-1], 2) if len(b[2:]) > 1 else 0
    return x, y

def decode_pair1(n):
    return decode_pair_helper(n, '0')

def decode_pair2(n):
    return decode_pair_helper(n, '1')

def decode_list(n):
    if n == 0:
        return []
    else:
        x, y = decode_pair1(n)
        return [x] + decode_list(y)

def decode_instruction(x):
    if x == 0:
        return 'HALT'
    else:
        y, z = decode_pair1(x)
        if y % 2 == 0:
            i = y / 2
            return 'R{}+ -> L{}'.format(i, z)
        else:
            i = (y - 1) / 2
            j, k = decode_pair2(z)
            return 'R{}- -> L{}, L{}'.format(i, j, k)

def decode_program(n):
    return map(decode_instruction, decode_list(n))


ex_program = [
    'R0- -> L0, L2',
    'HALT'
]
ex_n = 786432

cw_q1_program = """R1- -> L3, L5
R1- -> L4, L2
HALT
R1- -> L1, L2
R0+ -> L0
HALT""".split('\n')

cw_q2_n = 2 ** 94 * 16395

cw_q2_program = """R0- -> L3, L1
HALT
R0+ -> L0
R0- -> L0, L1""".split('\n')
