from math import floor

from inputReader import read_file


def make_set(cpt):
    ret_set = set()
    for x in cpt:
        ret_set.add(x)
    return ret_set


def get_common_letter(sack):
    left_cpt = sack[:floor(len(sack) / 2)]
    right_cpt = sack[floor(len(sack) / 2):]
    left_set = make_set(left_cpt)
    right_set = make_set(right_cpt)
    return left_set.intersection(right_set).pop()


def get_priority(letter):
    if ord(letter) >= 97:
        return ord(letter) - 96
    else:
        return ord(letter) - 38


def solve_pt_1(input_path):
    input_lines = read_file(input_path)
    print(sum([get_priority(get_common_letter(x)) for x in input_lines]))


def get_common_letter_of_three(lines, index):
    set_list = []
    for x in range(0, 3):
        set_list.append(make_set(lines[x + index]))

    return set_list[0].intersection(set_list[1]).intersection(set_list[2]).pop()


def solve_pt_2(input_path):
    input_lines = read_file(input_path)
    score = 0
    for x in range(0, len(input_lines), 3):
        score += get_priority(get_common_letter_of_three(input_lines, x))
    print(score)


day = "03"
sample_path = "inputDir/" + day + "_Sample.txt"
data_path = "inputDir/" + day + "_Data.txt"
# solve_pt_1(data_path)
solve_pt_2(data_path)
