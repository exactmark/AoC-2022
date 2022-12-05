from inputReader import read_file_with_strip


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
    outcome = ord(my_move[0]) - 23 - 64
    my_move = -1
    score = (outcome-1)*3
    if outcome == 1:
        my_move=op_move-1
        if my_move<1:
            my_move+=3
    elif outcome==2:
        my_move=op_move
    else:
        my_move=op_move+1
        if my_move>3:
            my_move-=3
    # print(my_move)
    # print(score)
    return score+my_move

def solve_pt_1(input_path):
    input_lines = read_file_with_strip(input_path)
    print(sum([get_pt1_rd_score(x) for x in input_lines]))


def solve_pt_2(input_path):
    input_lines = read_file_with_strip(input_path)
    for x in input_lines:
        get_pt2_rd_score(x)
    print(sum([get_pt2_rd_score(x) for x in input_lines]))


day = "02"
sample_path = "inputDir/" + day + "_Sample.txt"
data_path = "inputDir/" + day + "_Data.txt"
# solve_pt_1(data_path)
solve_pt_2(data_path)
