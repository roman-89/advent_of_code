
    
def intcode_program(intcode):
    i = 0  # start of the next optcode position 
    # instruction pointer
    while True:
        instruction = intcode[i]
        if instruction == 99:
            return intcode
        elif instruction == 1:
            intcode[intcode[i+3]] = intcode[intcode[i+1]] + intcode[intcode[i+2]]
        elif instruction == 2:
             intcode[intcode[i+3]] = intcode[intcode[i+1]] * intcode[intcode[i+2]]
        else:
            return [0]
        i = i + 4


assert intcode_program([1,0,0,0,99]) ==  [2,0,0,0,99]
assert intcode_program([2,3,0,3,99]) ==  [2,3,0,6,99]
assert intcode_program([2,4,4,5,99,0]) ==  [2,4,4,5,99,9801]
assert intcode_program([1,1,1,4,99,5,6,0,99]) ==  [30,1,1,4,2,5,6,0,99]


input = []
input[1] = 12
input[2] = 2
output = intcode_program(input)
print(output[0])


from copy import copy

for noun in range(99):
    for verb in range(99):
        input = copy(original_input)
        input[1] = noun
        input[2] = verb
        if intcode_program(input)[0] == 19690720:
            print(noun, verb)
            print(100*noun + verb)
