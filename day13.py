from inputReader import read_file_with_strip


def tri_order(left, right):
    if type(left) == type(right):
        if isinstance(left, int):
            if left < right:
                return -1
            elif left == right:
                return 0
            else:
                return 1
        else:
            if len(left) == 0 and len(right) == 0:
                return 0
            elif len(left) == 0:
                return -1
            elif len(right) == 0:
                return 1
            possible_end = tri_order(left[0], right[0])
            if possible_end != 0:
                return possible_end
            else:
                return tri_order(left[1:], right[1:])
    elif isinstance(left, int):
        return tri_order([left], right)
    else:
        return tri_order(left, [right])


def solve_pt_1(input_path):
    lines = read_file_with_strip(input_path)
    x = 0
    sum = 0
    while x < len(lines):
        left = eval(lines[x])
        right = eval(lines[x + 1])
        if tri_order(left, right) == 0:
            print("bad")
        if tri_order(left, right) < 0:
            print((x // 3) + 1)
            sum += (x // 3) + 1
        x += 3
    print(sum)


def solve_pt_2(input_path):
    lines = read_file_with_strip(input_path)
    x = 0
    all_lines = []
    all_lines.append([[2]])
    all_lines.append([[6]])
    while x < len(lines):
        left = eval(lines[x])
        right = eval(lines[x + 1])
        all_lines.append(left)
        all_lines.append(right)
        x += 3

    has_switched = True
    while has_switched:
        has_switched = False
        for x in range(len(all_lines) - 1):
            if tri_order(all_lines[x], all_lines[x + 1]) > 0:
                temp = all_lines[x]
                all_lines[x] = all_lines[x + 1]
                all_lines[x + 1] = temp
                has_switched = True
    # for single_line in all_lines:
    #     print(single_line)
    first_packet = 0
    second_packet = 0
    for x in range(len(all_lines)):
        if all_lines[x] == [[2]]:
            first_packet = x + 1
        if all_lines[x] == [[6]]:
            second_packet = x + 1
    print(first_packet * second_packet)


day = "13"
sample_path = "inputDir/" + day + "_Sample.txt"
data_path = "inputDir/" + day + "_Data.txt"
# solve_pt_1(data_path)
solve_pt_2(data_path)
