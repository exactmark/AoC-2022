from inputReader import read_file_with_strip


class Board:
    def __init__(self):
        self.headCoord = [0, 0]
        self.tailCoord = [0, 0]
        self.tailVisited = {}
        self.tailVisited["0,0"] = 1

    def maybe_move_tail(self):
        x_dist = abs(self.headCoord[0] - self.tailCoord[0])
        y_dist = abs(self.headCoord[1] - self.tailCoord[1])
        if y_dist > 1 or x_dist > 1:
            # print("must move")
            if x_dist > 0:
                if self.headCoord[0] > self.tailCoord[0]:
                    self.tailCoord[0] += 1
                else:
                    self.tailCoord[0] -= 1
            if y_dist > 0:
                if self.headCoord[1] > self.tailCoord[1]:
                    self.tailCoord[1] += 1
                else:
                    self.tailCoord[1] -= 1
            tailCoordText = str(self.tailCoord[0]) + "," + str(self.tailCoord[1])
            self.tailVisited[tailCoordText] = 1

    def process_move(self, line):
        direction = line.split(" ")[0]
        dist = int(line.split(" ")[1])
        for x in range(dist):
            print("new move")
            if direction == "U":
                self.headCoord[1] = self.headCoord[1] + 1
            if direction == "D":
                self.headCoord[1] = self.headCoord[1] - 1
            if direction == "R":
                self.headCoord[0] = self.headCoord[0] + 1
            if direction == "L":
                self.headCoord[0] = self.headCoord[0] - 1
            print("head:", self.headCoord[0], ",", self.headCoord[1])
            self.maybe_move_tail()
            print("tail:", self.tailCoord[0], ",", self.tailCoord[1])


def solve_pt_1(input_path):
    lines = read_file_with_strip(input_path)
    board = Board()
    for line in lines:
        board.process_move(line)
    print(sum(board.tailVisited.values()))


def solve_pt_2(input_path):
    lines = read_file_with_strip(input_path)


day = "09"
sample_path = "inputDir/" + day + "_Sample.txt"
data_path = "inputDir/" + day + "_Data.txt"
solve_pt_1(data_path)
