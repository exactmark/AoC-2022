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
        for x in data:
            for y in x:
                print(y)
            print(x)
            if x == "\n":
                break


def solve_pt_1(input_path):
    input_lines = read_file(input_path)
    warehouse = Warehouse()
    warehouse.populate_floor(input_lines)


def solve_pt_2(input_path):
    input_lines = read_file(input_path)


day = "05"
sample_path = "inputDir/" + day + "_Sample.txt"
data_path = "inputDir/" + day + "_Data.txt"
solve_pt_1(sample_path)
