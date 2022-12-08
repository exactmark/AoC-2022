from inputReader import read_file_with_strip


class Tree:
    def __init__(self, height, x, y):
        self.height = height
        self.shade_from = {}
        self.blocked_by = {}
        self.visible = True
        self.coords = [x, y]
        self.scenic = 0

    def set_tree_visibility(self):
        for dir_height in self.shade_from.values():
            if dir_height < self.height:
                return
        self.visible = False


class Forest:
    def __init__(self):
        self.trees = []

    def add_trees(self, lines):
        self.trees = []
        y = 0
        for single_line in lines:
            this_line = []
            x = 0
            for single_tree in single_line:
                a_tree = Tree(int(single_tree), x, y)
                this_line.append(a_tree)
                x += 1
            self.trees.append(this_line)
            y += 1
        self.set_visibility()

    def set_visibility(self):
        for y in range(len(self.trees)):
            lowest_west = -1
            blocker = [0, y]
            for x in range(len(self.trees[y])):
                this_tree = self.trees[y][x]
                this_tree.shade_from["w"] = lowest_west
                this_tree.blocked_by["w"] = blocker
                if this_tree.height > lowest_west:
                    lowest_west = this_tree.height
                    blocker = [x, y]
            lowest_east = -1
            blocker = [len(self.trees) - 1, y]
            for x in range(len(self.trees[y]) - 1, 0 - 1, -1):
                this_tree = self.trees[y][x]
                this_tree.shade_from["e"] = lowest_east
                this_tree.blocked_by["e"] = blocker
                if this_tree.height > lowest_east:
                    lowest_east = this_tree.height
                    blocker = [x, y]
        for x in range(len(self.trees[0])):
            lowest_north = -1
            blocker = [x, 0]
            for y in range(len(self.trees)):
                this_tree = self.trees[y][x]
                this_tree.shade_from["n"] = lowest_north
                this_tree.blocked_by["n"] = blocker
                if this_tree.height > lowest_north:
                    lowest_north = this_tree.height
                    blocker = [x, y]
            lowest_south = -1
            blocker = [x, len(self.trees) - 1]
            for y in range(len(self.trees) - 1, 0 - 1, -1):
                this_tree = self.trees[y][x]
                this_tree.shade_from["s"] = lowest_south
                this_tree.blocked_by["s"] = blocker
                if this_tree.height > lowest_south:
                    blocker = [x, y]
                    lowest_south = this_tree.height
        for y in range(len(self.trees)):
            for x in range(len(self.trees[y])):
                this_tree = self.trees[y][x]
                this_tree.set_tree_visibility()
                this_tree.scenic = self.calc_tree_scenic(x, y)
                # print(x, ":", y, ":", this_tree.scenic)

    def calc_tree_scenic(self, tree_x, tree_y):
        # calc north dist
        tree_height = self.trees[tree_y][tree_x].height
        n_dist = 0
        y = tree_y - 1
        x = tree_x
        while y > -1:
            n_dist += 1
            if self.trees[y][x].height >= tree_height:
                break
            y -= 1
        s_dist = 0
        y = tree_y + 1
        x = tree_x
        while y < len(self.trees):
            s_dist += 1
            if self.trees[y][x].height >= tree_height:
                break
            y += 1
        w_dist = 0
        y = tree_y
        x = tree_x - 1
        while x > -1:
            w_dist += 1
            if self.trees[y][x].height >= tree_height:
                break
            x -= 1
        e_dist = 0
        y = tree_y
        x = tree_x + 1
        while x < len(self.trees[y]):
            e_dist += 1
            if self.trees[y][x].height >= tree_height:
                break
            x += 1
        return n_dist * s_dist * w_dist * e_dist

    def print_visibility(self):
        for y in range(len(self.trees)):
            line = ""
            for x in range(len(self.trees[y])):
                if self.trees[y][x].visible == True:
                    line += "T"
                else:
                    line += "F"
            print(line)


def solve_pt_1(input_path):
    lines = read_file_with_strip(input_path)
    forest = Forest()
    forest.add_trees(lines)
    forest.print_visibility()
    visible = 0
    for y in range(len(forest.trees)):
        for x in range(len(forest.trees[y])):
            if forest.trees[y][x].visible:
                visible += 1
    print(visible)


def solve_pt_2(input_path):
    lines = read_file_with_strip(input_path)
    forest = Forest()
    forest.add_trees(lines)
    forest.print_visibility()
    best_scenic = 0
    for y in range(len(forest.trees)):
        for x in range(len(forest.trees[y])):
            if forest.trees[y][x].scenic>best_scenic:
                best_scenic = forest.trees[y][x].scenic
    print(best_scenic)


day = "08"
sample_path = "inputDir/" + day + "_Sample.txt"
data_path = "inputDir/" + day + "_Data.txt"
solve_pt_2(data_path)
