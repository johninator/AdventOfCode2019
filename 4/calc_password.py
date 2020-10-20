
def main():
    
    number_begin = 273025
    number_end = 767253

    passwords = []

    for number in range(number_begin, number_end+1):
        number_list = [int(d) for d in str(number)]
        if check_for_two_digits(number_list):
            if check_for_ascending_numbers(number_list):
                if check_for_two_individual_digits(number_list):
                    passwords.append(number_list)
    
    print("no of passwords: {}".format(len(passwords)))
    # print("found passwords: ")
    # for pw in passwords:
    #     print(pw)


def check_for_two_individual_digits(number):
    # check if at least two adjacent digits are the same
    digit_last = -1
    stop_at_id = 0

    for digit_id in range(0, len(number)):

        if digit_id < stop_at_id:
            continue
        
        digit = number[digit_id]


        if digit_id < len(number) - 1:
            digit_next = number[digit_id+1]
        else:
            digit_next = -1

        # print("digit: {}".format(digit))
        # print("digit next: {}".format(digit_next))
        # print("digit last: {}".format(digit_last))


        if digit == digit_last:
            if digit != digit_next:
                return True
            else: # skip this block since it's longer than 2
                while(True):
                    if digit_id == len(number) - 1:
                        return False
                    else:                    
                        digit_id = digit_id + 1

                    digit_temp = number[digit_id]
                    if digit_temp != digit:
                        stop_at_id = digit_id
                        break

        digit_last = digit
    return False

def check_for_ascending_numbers(number):
    # check if digits are ascending
    digit_last = -1
    for digit in number:
        if digit < digit_last:
            return False
        digit_last = digit
    return True    

def check_for_two_digits(number):
    # check if at least two adjacent digits are the same
    digit_last = -1
    for digit in number:
        if digit == digit_last:
            return True
        digit_last = digit
    return False




main()
