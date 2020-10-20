import csv
import math


def main():
    # read values from file
    input = read_values('integers.csv')
    print("input: {}".format(input))
    # compute code recursively
    process_input_at_id(0, input)
    print("output: {}".format(input))
       
         
def read_values(filename):
   with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            res = [int(i) for i in row] 
            return res

def process_input_at_id(id, input):
    print("current input: {}".format(input[id]))
    
    if input[id] == 99: # stop command
        print("stop command")
        return;
    elif input[id] == 1: # add command
        print("add command")
        res = input[input[id+1]] + input[input[id+2]]
        input[input[id+3]] = res
        process_input_at_id(id+4, input)
    elif input[id] == 2: # multiply command
        print("mul command")
        res = input[input[id+1]] * input[input[id+2]]
        input[input[id+3]] = res
        process_input_at_id(id+4, input)
    else:
        print("error: wrong command id")
        
         
main()