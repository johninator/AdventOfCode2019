import csv
import math


def main():
    # read values from file
    input_original = read_values('integers.csv')
    # print("input_original: {}".format(input_original))

    # compute code recursively
    process_input_at_id(0, input_original)


def read_values(filename):
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            res = [int(i) for i in row]
            return res


def parse_parameters(opcode, id, input):
    if opcode == "opcode_add":
        return input[id:id+3]
    elif opcode == "opcode_mul":
        return input[id:id+3]
    elif opcode == "opcode_input":
        return input[id:id+1]
    elif opcode == "opcode_output":
        return input[id:id+1]
    elif opcode == "opcode_jump_if_true":
        return input[id:id+2]
    elif opcode == "opcode_jump_if_false":
        return input[id:id+2]
    elif opcode == "opcode_less_than":
        return input[id:id+3]
    elif opcode == "opcode_equals":
        return input[id:id+3]
    else:  # opcode == "opcode_stop":
        return []


def opcode_add(par_mode, id, input):
    vars = pars_par_mode(par_mode, id, input)
    # perform addition with vars, always in position mode
    input[input[id+3]] = vars[0] + vars[1]


def opcode_mul(par_mode, id, input):
    vars = pars_par_mode(par_mode, id, input)
    # perform addition with vars, always in position mode
    input[input[id+3]] = vars[0] * vars[1]


def opcode_input(id, input, input_real):
    input[input[id+1]] = input_real


def opcode_output(par_mode, id, input):
    #print("par mode: {}".format(par_mode))
    if len(par_mode) == 0 or par_mode[0] == 0:
        print("opcode output: {}".format(input[input[id+1]]))
    else:
        print("opcode output: {}".format(input[id+1]))

# opcode 5


def opcode_jump_if_true(par_mode, id, input):
    vars = pars_par_mode(par_mode, id, input)
    # return new id
    if vars[0] != 0:
        return vars[1]
    else:
        return id

# opcode 6


def opcode_jump_if_false(par_mode, id, input):
    vars = pars_par_mode(par_mode, id, input)
    # return new id
    if vars[0] == 0:
        return vars[1]
    else:
        return id

# opcode 7


def opcode_less_than(par_mode, id, input):
    vars = pars_par_mode(par_mode, id, input)
    if vars[0] < vars[1]:
        input[input[id+3]] = 1
    else:
        input[input[id+3]] = 0

# opcode 8


def opcode_equals(par_mode, id, input):
    vars = pars_par_mode(par_mode, id, input)
    if vars[0] == vars[1]:
        input[input[id+3]] = 1
    else:
        input[input[id+3]] = 0


def pars_par_mode(par_mode, id, input):
    vars = []
    for i in range(0, 2):
        # get param mode
        par_mode_i = 0
        if i < len(par_mode):
            par_mode_i = par_mode[i]
        # set variables depending on param mode
        if par_mode_i == 0:  # position mode
            vars.append(input[input[id+1+i]])
        else:  # value mode
            vars.append(input[id+1+i])
    return vars


def opcode_stop():
    return


def process_opcode(opcode, par_mode, id, input):
    id_new = id
    if opcode == "opcode_add":
        opcode_add(par_mode, id, input)
    elif opcode == "opcode_mul":
        opcode_mul(par_mode, id, input)
    elif opcode == "opcode_input":
        opcode_input(id, input, 5)
    elif opcode == "opcode_jump_if_true":
        id_new = opcode_jump_if_true(par_mode, id, input)
    elif opcode == "opcode_jump_if_false":
        id_new = opcode_jump_if_false(par_mode, id, input)
    elif opcode == "opcode_less_than":
        opcode_less_than(par_mode, id, input)
    elif opcode == "opcode_equals":
        opcode_equals(par_mode, id, input)
    else:  # opcode == "opcode_output"
        opcode_output(par_mode, id, input)
    return id_new


def process_command_code(number_list):
    # get opcode from last two digits
    if len(number_list) < 2:
        last_two_digits = [0, number_list[0]]
    else:
        last_two_digits = number_list[len(number_list)-2:]

    opcode = ""

    if last_two_digits[1] == 1:
        opcode = "opcode_add"
    elif last_two_digits[1] == 2:
        opcode = "opcode_mul"
    elif last_two_digits[1] == 3:
        opcode = "opcode_input"
    elif last_two_digits[1] == 4:
        opcode = "opcode_output"
    elif last_two_digits[1] == 5:
        opcode = "opcode_jump_if_true"
    elif last_two_digits[1] == 6:
        opcode = "opcode_jump_if_false"
    elif last_two_digits[1] == 7:
        opcode = "opcode_less_than"
    elif last_two_digits[1] == 8:
        opcode = "opcode_equals"
    else:  # 99
        opcode = "opcode_stop"

    # get parameter mode from left over digits
    par_mode = []
    for digit in reversed(number_list[0: len(number_list)-2]):
        par_mode.append(digit)

    return opcode, par_mode


def process_input_at_id(id, input):
    # convert number to digit list
    command = [int(d) for d in str(input[id])]
    opcode, par_mode = process_command_code(command)
    print("opcode: " + opcode)
    if opcode == "opcode_stop":
        print("stop")
        return
    else:
        id_new = process_opcode(opcode, par_mode, id, input)

    # if new id is returned from jump opcode, use it
    # otherwise, go to next opcode
    if id_new != id:
        id = id_new
    else:
        parameters = parse_parameters(opcode, id, input)
        #print("length of parameters: {}".format(len(parameters)))
        id = id + len(parameters) + 1

    process_input_at_id(id, input)


main()
