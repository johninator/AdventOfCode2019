class Tree:
    def __init__(self, name):
        self.name = name
        self.children = []
        # self.parent

    def add_simple(self, name):
        already_existing = False
        for child in self.children:
            if child.name == name:
                already_existing = True
        # add child if it's not yet existing
        if not already_existing:
            child = Tree(name)
            self.children.append(child)
            child.parent = self
            return True

        #print("Error: child already existing")
        return False

    def add(self, parent_name, child_name):
        # traverse through all children to find the parent node
        found, parent_object = self.search_down(parent_name)
        if found == True:
            return parent_object.add_simple(child_name)
        return False

    def search_between(self, name1, name2):
        # print("start search between: {} and {}".format(name1, name2))
        # finding starting object
        success, object1 = self.search_down(name1)
        if success:
            # print("found start at object: {}".format(object1.name))
            found, steps = object1.search_down_and_up(name2, 0, False)
            # print("found {} ? : {}".format(name2, found))
            return steps-1
        return -1

    def search_down_and_up(self, name, steps, down):
        # print("at {} with {} steps, mode: {}, parent: {}".format(
        #     self.name, steps, down, self.parent.name))
        steps = steps + 1
        if self.name == name:
            return True, steps
        else:
            for child in self.children:
                success, steps = child.search_down_and_up(name, steps, True)
                if success:
                    return success, steps
        # current children search was not successful, go one level up
        # print("reduce steps")
        steps = steps - 1

        if not down:  # target not found at current level, restart search at parent
            # print("start parent search")
            steps = steps + 1
            success, steps = self.parent.search_down_and_up(name, steps, False)
            if success:
                return success, steps

        return False, steps

    def search_down(self, parent_name):
        # traverse through all children to find the parent node
        if self.name == parent_name:
            return True, self
        else:
            for child in self.children:
                success, parent_object = child.search_down(parent_name)
                if success:
                    return success, parent_object
        return False, Tree("")

    def print_children(self, depth):
        for child in self.children:
            string_header = "-" * depth
            print(string_header + str(child.name))
            child.print_children(depth+1)

    def print(self):
        print(self.name)
        self.print_children(1)

    def count_leaves(self):
        count = 0
        for child in self.children:
            if len(child.children) > 0:
                count = count + child.count_relations()
            else:  # no children
                count = count + 1
        return count

    def count_depths_at(self, depth):
        count = 0
        for child in self.children:
            count = count + depth
            if len(child.children) > 0:
                count = count + child.count_depths_at(depth+1)

        return count

    def count_depths(self):
        return self.count_depths_at(1)
