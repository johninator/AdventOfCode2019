class Tree:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_simple(self, name):
        already_existing = False
        for child in self.children:
            if child.name == name:
                already_existing = True
        # add child if it's not yet existing
        if not already_existing:
            self.children.append(Tree(name))
            return True

        #print("Error: child already existing")
        return False

    def add(self, parent_name, child_name):
        # traverse through all children to find the parent node

        if self.name == parent_name:
            return self.add_simple(child_name)
        else:
            success = False
            for child in self.children:
                success = success or child.add(parent_name, child_name)
            return success

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
