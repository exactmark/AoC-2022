from inputReader import read_file_with_strip


class Cave:
    def __init__(self):
        self.sand_start = [500, 0]
        self.board = []
        self.max_x = 0
        self.max_y = 0
        self.min_x = 0

    def print_board(self):
        for row in self.board:
            print("".join(row))
        print("")

    def load_board(self, lines):
        max_x = 0
        max_y = 0
        min_x = int(lines[0].split(" -> ")[0].split(",")[0])
        rock_points = []
        for single_line in lines:
            this_rock_text = single_line.split(" -> ")
            this_rock_points = []
            for rock_point in this_rock_text:
                rock_point_x = int(rock_point.split(",")[0])
                rock_point_y = int(rock_point.split(",")[1])
                this_rock_points.append([rock_point_x, rock_point_y])
                if rock_point_x > max_x:
                    max_x = rock_point_x
                if rock_point_y > max_y:
                    max_y = rock_point_y
                if rock_point_x < min_x:
                    min_x = rock_point_x
            rock_points.append(this_rock_points)
        # add some buffer
        self.max_x = max_x + 2
        self.max_y = max_y + 2
        self.min_x = min_x - 2
        row_size = self.max_x - self.min_x

        for y in range(self.max_y):
            this_row = []
            for x in range(row_size):
                this_row.append(".")
            self.board.append(this_row)

        for rock_form in rock_points:
            for i in range(len(rock_form) - 1):
                x = rock_form[i][0]
                y = rock_form[i][1]
                dx, dy = get_dir(rock_form[i], rock_form[i + 1])
                self.board[y][x - self.min_x] = "#"
                while [x, y] != rock_form[i + 1]:
                    y += dy
                    x += dx
                    self.board[y][x - self.min_x] = "#"

        self.print_board()

    def add_all_sand(self):
        added_sand = 0
        while self.add_sand():
            added_sand += 1
            self.print_board()
        print(added_sand)

    def add_sand(self):
        x, y = self.sand_start
        x = x - self.min_x
        can_move = True
        while can_move:
            if y >= self.max_y-1:
                return False
            if self.board[y + 1][x] == ".":
                y += 1
            elif self.board[y + 1][x - 1] == ".":
                y += 1
                x -= 1
            elif self.board[y + 1][x + 1] == ".":
                y += 1
                x += 1
            else:
                can_move = False
        self.board[y][x] = "o"
        return True


def get_dir(pt1, pt2):
    dx = pt2[0] - pt1[0]
    if dx != 0:
        dx = dx // abs(dx)
    dy = pt2[1] - pt1[1]
    if dy != 0:
        dy = dy // abs(dy)
    return dx, dy


def solve_pt_1(input_path):
    lines = read_file_with_strip(input_path)
    cave = Cave()
    cave.load_board(lines)
    cave.add_all_sand()


def solve_pt_2(input_path):
    lines = read_file_with_strip(input_path)


day = "14"
sample_path = "inputDir/" + day + "_Sample.txt"
data_path = "inputDir/" + day + "_Data.txt"
solve_pt_1(data_path)
