from tree import Tree
import csv


def main():
    map = read_values("map.csv")
    map_tree = build_tree_from_map(map)
    # map_tree.print()
    num_switches = find_switches_between(map_tree, "YOU", "SAN")
    print("switches: {}".format(num_switches))


def read_values(filename):
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=")")
        map = []
        for row in reader:
            map.append(row)
        return map


def find_switches_between(tree, name1, name2):
    # find tree node for name1
    return tree.search_between(name1, name2)


def build_tree_from_map(map):
    tree = Tree("COM")
    new_orbit_added = True
    while new_orbit_added:
        # print("next round -------------------------------")
        new_orbit_added = False
        for relation in map:
            parent = relation[0]
            child = relation[1]
            new_orbit_added = tree.add(parent, child) or new_orbit_added
            # print("added {} to {}, result: {}".format(
            #     child, parent, new_orbit_added))
            # if at least one new orbit has been found, continue
    return tree


def count_orbits(map_tree):
    return map_tree.count_depths()


main()
