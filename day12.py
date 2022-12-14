from inputReader import read_file_with_strip


class Cell:
    def __init__(self, x, y, height):
        self.neighbors = []
        self.id = [x, y]
        self.best_route = []
        self.is_start = False
        self.is_end = False
        if height == "E":
            self.is_end = True
            self.height = 25
        elif height == "S":
            self.is_start = True
            self.height = 0
        else:
            self.height = ord(height) - 97
        # print(self.height)


class Board:
    def __init__(self):
        self.field = []
        self.start_cell = None
        self.end_cell = None
        self.all_cells = []

    def load_board(self, lines):
        self.field = []
        for y in range(0, len(lines)):
            this_row = []
            for x in range(0, len(lines[y])):
                new_cell = Cell(x, y, lines[y][x])
                this_row.append(new_cell)
                self.all_cells.append(new_cell)
            self.field.append(this_row)
        for y in range(len(self.field)):
            for x in range(len(self.field[y])):
                if self.field[y][x].is_start:
                    self.start_cell = self.field[y][x]
                elif self.field[y][x].is_end:
                    self.end_cell = self.field[y][x]
                for neighbor_y in [-1, 0, 1]:
                    for neighbor_x in [-1, 0, 1]:
                        if y + neighbor_y in range(len(self.field)) and x + neighbor_x in range(
                                len(self.field[y])) and abs(neighbor_x + neighbor_y) == 1:
                            self.field[y][x].neighbors.append(self.field[y + neighbor_y][x + neighbor_x])


def can_travel(source: Cell, dest: Cell):
    if source.height + 1 >= dest.height:
        return True
    return False


def find_solution_pt1(board):
    visited_cells = []
    solutions = []
    solutions.append([board.start_cell])
    visited_cells.append(board.start_cell)
    solution_found = False
    while not solution_found:
        previous_visited_count = len(visited_cells)
        next_solution_list = []
        for single_solution in solutions:
            for neighbor in single_solution[-1].neighbors:
                if can_travel(single_solution[-1], neighbor) and not neighbor in visited_cells:
                    visited_cells.append(neighbor)
                    new_solution = single_solution.copy()
                    new_solution.append(neighbor)
                    next_solution_list.append(new_solution)
                    if neighbor.is_end:
                        return new_solution
        if len(visited_cells) == previous_visited_count:
            return None
        solutions = next_solution_list
        # print(solutions)


def solve_pt_1(input_path):
    lines = read_file_with_strip(input_path)
    board = Board()
    board.load_board(lines)
    print("loaded")
    solution = find_solution_pt1(board)
    print(len(solution) - 1)


def solve_pt_2(input_path):
    lines = read_file_with_strip(input_path)
    board = Board()
    board.load_board(lines)
    print("loaded")
    a_list = []
    for single_cell in board.all_cells:
        if single_cell.height == 0:
            a_list.append(single_cell)
    # previous best solution + 1
    best_solution = 463
    for x in range(len(a_list)):
        board.start_cell = a_list[x]
        solution = find_solution_pt1(board)
        print(x, " of ", len(a_list))
        if solution:
            if len(solution) < best_solution:
                best_solution = len(solution)
    print(best_solution - 1)


day = "12"
sample_path = "inputDir/" + day + "_Sample.txt"
data_path = "inputDir/" + day + "_Data.txt"
solve_pt_2(data_path)
