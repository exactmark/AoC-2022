from inputReader import read_file


class CrateStack:

    def __init__(self):
        self.crates = []

    def pop_crate(self):
        return self.crates.pop()

    def add_crate(self, crate):
        self.crates.append(crate)


class Warehouse:
    def __init__(self):
        self.stacks = []

    def populate_floor(self, data):
        x = 1
        while x < len(data[0]):
            self.stacks.append([])
            x += 4
        for x in data:
            y = 0
            ptr = y * 4 + 1
            if x[ptr] == "1":
                break
            while ptr < len(x):
                if x[ptr] != " ":
                    self.stacks[y].append(x[ptr])
                y += 1
                ptr = y * 4 + 1
        for x in range(len(self.stacks)):
            self.stacks[x].reverse()

    def do_move(self, move):
        num_moves = int(move.split(" ")[1])
        from_stack = int(move.split(" ")[3]) - 1
        to_stack = int(move.split(" ")[5]) - 1
        for x in range(num_moves):
            self.stacks[to_stack].append(self.stacks[from_stack].pop())

    def do_pt2_move(self, move):
        move_size = int(move.split(" ")[1])
        from_stack = int(move.split(" ")[3]) - 1
        to_stack = int(move.split(" ")[5]) - 1
        move_stack = []
        for x in range(move_size):
            move_stack = [self.stacks[from_stack].pop()] + move_stack
        self.stacks[to_stack] = self.stacks[to_stack] + move_stack


def solve_pt_1(input_path):
    input_lines = read_file(input_path)
    warehouse = Warehouse()
    warehouse.populate_floor(input_lines)
    x = 0
    while input_lines[x] != "\n":
        x += 1
    x += 1
    while x < len(input_lines):
        warehouse.do_move(input_lines[x])
        x += 1
    final_string = ""
    for x in warehouse.stacks:
        final_string += x.pop()
    print(final_string)


def solve_pt_2(input_path):
    input_lines = read_file(input_path)
    warehouse = Warehouse()
    warehouse.populate_floor(input_lines)
    x = 0
    while input_lines[x] != "\n":
        x += 1
    x += 1
    while x < len(input_lines):
        warehouse.do_pt2_move(input_lines[x])
        x += 1
    final_string = ""
    for x in warehouse.stacks:
        final_string += x.pop()
    print(final_string)


day = "05"
sample_path = "inputDir/" + day + "_Sample.txt"
data_path = "inputDir/" + day + "_Data.txt"
# solve_pt_1(data_path)
solve_pt_2(data_path)
