import numpy as np
import csv


def main():
    # read vectors as strings from csv file
    raw_vecs = read_csv('vectors.csv')

    # convert vectors into integer tuples for horizontal and vertical vectors
    hor_vecs1, vert_vecs1 = split_vecs(raw_vecs[0])
    hor_vecs2, vert_vecs2 = split_vecs(raw_vecs[1])

    # find crossings between both sets
    crossings_1 = find_crossings(hor_vecs1, vert_vecs2)
    crossings_2 = find_crossings(hor_vecs2, vert_vecs1)
    crossings_1.extend(crossings_2)

    # find steps the wrie takes for each intersection
    steps_1 = find_steps(crossings_1, raw_vecs[0])
    steps_2 = find_steps(crossings_1, raw_vecs[1])

    print("steps_1: {}".format(steps_1))
    print("steps_2: {}".format(steps_2))
    # find lowest number of combined steps
    steps_lowest = find_lowest_combined_steps(steps_1, steps_2)
    print("lowest combined steps: {}".format(steps_lowest))


def find_lowest_combined_steps(steps_1, steps_2):
    if len(steps_1) != len(steps_2):
        print("error, steps not equally long: {} {}".format(
            len(steps_1), len(steps_2)))
        return

    steps_added = np.array(steps_1) + np.array(steps_2)
    print("steps added: {}".format(steps_added))
    return min(steps_added)


def find_steps(crossings, vecs):
    # for each crossing iterate over vec until crossing is reached
    steps_list = []
    for crossing in crossings:
        reached = False
        x = 0
        y = 0
        steps = 0

        for vec in vecs:
            if not reached:
                # perform step to next position
                x_next, y_next = step(vec, x, y)
                # check if crossing has been reached
                crossing_reached = check_for_reached_crossing(
                    x_next, y_next, x, y, crossing)

                if crossing_reached:
                    steps = steps + man_dist(crossing[0], crossing[1], x, y)
                    steps_list.append(steps)
                    reached = True
                    break
                else:
                    steps = steps + man_dist(x_next, y_next, x, y)
                    x = x_next
                    y = y_next
    return steps_list


def man_dist(x1, y1, x2, y2):
    dist_x = abs(x1-x2)
    dist_y = abs(y1-y2)
    return dist_x+dist_y


def check_for_reached_crossing(x_next, y_next, x, y, crossing):
    if x_next == x:
        # vertical step
        y_h = max(y, y_next)
        y_l = min(y, y_next)
        if x == crossing[0] and crossing[1] < y_h and crossing[1] > y_l:
            return True
    else:  # y_next == y
        # horizontal step
        x_h = max(x, x_next)
        x_l = min(x, x_next)
        if y == crossing[1] and crossing[0] < x_h and crossing[0] > x_l:
            return True
    # if no crossing has been reached
    return False


def step(vec, x, y):
    offset = int(vec[1:])
    if vec[0] == 'U':
        # print("up by: {}".format(offset))
        return x, (y+offset)
    elif vec[0] == 'D':
        # print("down by: {}".format(offset))
        return x, (y-offset)
    elif vec[0] == 'R':
        # print("right by: {}".format(offset))
        return (x+offset), y
    else:  # 'L'
        # print("left by: {}".format(offset))
        return (x-offset), y


def find_closest_crossing(crossings):
    x_crossing = crossings[1][0]
    y_crossing = crossings[1][1]
    print("initial crossing: {}, {}".format(x_crossing, y_crossing))
    man_dist_min = abs(x_crossing) + abs(y_crossing)

    for crossing in crossings:
        man_dist = abs(crossing[0]) + abs(crossing[1])
        if man_dist < man_dist_min and man_dist > 100:
            x_crossing = crossing[0]
            y_crossing = crossing[1]
            man_dist_min = man_dist

    return man_dist_min


def find_crossings(hor_vecs, vert_vecs):
    crossings = []
    for hor_vec in hor_vecs:
        for vert_vec in vert_vecs:
            # compare each horizontal to each vertical vector
            y_hor = hor_vec[0]
            y_vert_l = vert_vec[1]
            y_vert_h = vert_vec[2]

           # print("hor vec: {}".format(hor_vec))
           # print("vert vec: {}".format(vert_vec))

            # check 1:
            if y_hor <= y_vert_h and y_hor >= y_vert_l:
                x_vert = vert_vec[0]
                x_hor_l = hor_vec[1]
                x_hor_h = hor_vec[2]
                # check 2:
                if x_vert <= x_hor_h and x_vert >= x_hor_l:
                    # crossing found
                    x_crossing = y_hor
                    y_crossing = x_vert
                    crossings.append([x_vert, y_hor])
    return crossings


def split_vecs(vecs):
    hor_vecs = []
    vert_vecs = []
    x = 0
    y = 0

    for vec in vecs:
        # check direction of current vector
        offset = int(vec[1:])
        if vec[0] == 'U':
            vec_new = [x, y, y+offset]
            vert_vecs.append(vec_new)
            y = y + offset
        elif vec[0] == 'D':
            vec_new = [x, y-offset, y]
            vert_vecs.append(vec_new)
            y = y - offset
        elif vec[0] == 'R':
            vec_new = [y, x, x+offset]
            hor_vecs.append(vec_new)
            x = x + offset
        else:  # 'L'
            vec_new = [y, x-offset, x]
            hor_vecs.append(vec_new)
            x = x - offset

 #   print("hor vecs: {}", hor_vecs)
 #   print("vert vecs: {}", vert_vecs)

    return hor_vecs, vert_vecs


def read_csv(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        vecs = []
        for row in reader:
            vecs.append(row)
        return vecs


main()
