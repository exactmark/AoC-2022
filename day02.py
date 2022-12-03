from inputReader import read_file


def get_pt1_rd_score(line):
    op_move, my_move = str(line).split(" ")
    op_move = ord(op_move[0]) - 64
    my_move = ord(my_move[0]) - 23 - 64
    score = my_move
    # print(op_move)
    # print(my_move)
    if op_move == my_move:
        # print("draw")
        score+=3
    elif op_move + 1 == my_move or op_move - 2 == my_move:
        # print("win")
        score+=6
    elif op_move - 1 == my_move or op_move + 2 == my_move:
        # print("lose")
        score+=0
    else:
        print("No wld")
        raise Exception("No wld")
    return score

def get_pt2_rd_score(line):
    op_move, my_move = str(line).split(" ")
    op_move = ord(op_move[0]) - 64
    my_move = ord(my_move[0]) - 23 - 64
    score = my_move
    # print(op_move)
    # print(my_move)
    if op_move == my_move:
        # print("draw")
        score+=3
    elif op_move + 1 == my_move or op_move - 2 == my_move:
        # print("win")
        score+=6
    elif op_move - 1 == my_move or op_move + 2 == my_move:
        # print("lose")
        score+=0
    else:
        print("No wld")
        raise Exception("No wld")
    return score

def solve_pt_1(input_path):
    input_lines = read_file(input_path)
    for x in input_lines:
        get_pt1_rd_score(x)
    print(sum([get_pt1_rd_score(x) for x in input_lines]))


def solve_pt_2(input_path):
    input_lines = read_file(input_path)


day = "02"
sample_path = "inputDir/" + day + "_Sample.txt"
data_path = "inputDir/" + day + "_Data.txt"
solve_pt_1(data_path)
# solve_pt_2(sample_path)
