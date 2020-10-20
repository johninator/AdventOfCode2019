import csv
import math



def main():
    goal = 19690720
    # read values from file
    input_original = read_values('integers.csv')
    print("input_original: {}".format(input_original))
    
    noun = range(100)
    verb = range(100)
    
    for n in noun:
        for v in verb:
            input_copy = input_original.copy()
            input_copy[1] = n;
            input_copy[2] = v; 
            
            print("input_copy[0-2]: {}, {}, {}".format(input_copy[0], input_copy[1], input_copy[2]))
            
            # compute code recursively
            process_input_at_id(0, input_copy)
            print("input_copy[0]: {}".format(input_copy[0]))
            
            
            if input_copy[0] == goal:
                print("n: {} v: {}".format(n,v))
                break          
                
           
def read_values(filename):
   with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            res = [int(i) for i in row] 
            return res

def process_input_at_id(id, input):
    if input[id] == 99: # stop command
        #print("stop command")
        return;
    elif input[id] == 1: # add command
        #print("add command")
        res = input[input[id+1]] + input[input[id+2]]
        input[input[id+3]] = res
        process_input_at_id(id+4, input)
    elif input[id] == 2: # multiply command
        #print("mul command")
        res = input[input[id+1]] * input[input[id+2]]
        input[input[id+3]] = res
        process_input_at_id(id+4, input)
    else:
        #print("error: wrong command id")
        return
        
         
main()