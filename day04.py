from inputReader import read_file


def make_ranges(line):
    mod_line = line.replace("-", ",")
    mod_line = mod_line.split(",")
    mod_line = [int(x) for x in mod_line]
    return mod_line[0:2], mod_line[2:4]


def range_contains_range(first_range, second_range):
    if first_range[0] <= second_range[0] and first_range[1] >= second_range[1]:
        return True
    return False


def solve_pt_1(input_path):
    input_lines = read_file(input_path)
    contained_pairs = 0
    for single_line in input_lines:
        range1, range2 = make_ranges(single_line)
        if range_contains_range(range1, range2) or range_contains_range(range2, range1):
            contained_pairs += 1
    print(contained_pairs)


def solve_pt_2(input_path):
    input_lines = read_file(input_path)
    contained_pairs = 0
    for single_line in input_lines:
        range1, range2 = make_ranges(single_line)
        set1 = set(range(range1[0], range1[1] + 1))
        set2 = set(range(range2[0], range2[1] + 1))
        if len(set1.intersection(set2)) > 0:
            contained_pairs += 1
    print(contained_pairs)


day = "04"
sample_path = "inputDir/" + day + "_Sample.txt"
data_path = "inputDir/" + day + "_Data.txt"
# solve_pt_1(data_path)
solve_pt_2(data_path)
