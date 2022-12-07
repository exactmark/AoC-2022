from inputReader import read_file_with_strip

def is_unique(word):
    letter_set = set([x for x in word])
    if len(letter_set)==len(word):
        return True
    return False

def solve_pt_1(input_path):
    input_lines = read_file_with_strip(input_path)
    for line in input_lines:
        x=4
        while not is_unique(line[x-4:x]):
            x+=1
        print(x)


def solve_pt_2(input_path):
    input_lines = read_file_with_strip(input_path)
    marker_size = 14
    for line in input_lines:
        x=marker_size
        while not is_unique(line[x-marker_size:x]):
            x+=1
        print(x)

day = "06"
sample_path = "inputDir/" + day + "_Sample.txt"
data_path = "inputDir/" + day + "_Data.txt"
solve_pt_1(data_path)
solve_pt_2(data_path)
