from math import floor

from inputReader import read_file_with_strip


class Monkey:
    def __init__(self, monkey_lines):
        print(monkey_lines)
        self.items_inspected = 0
        # Monkey 0:
        self.monkey_num = int(monkey_lines[0][:len(monkey_lines[0]) - 1].split(" ")[1])
        # Starting items: 79, 98
        new_item_list = monkey_lines[1].split(": ")[1]
        self.item_list = [int(x) for x in new_item_list.split(", ")]
        # Operation: new = old * 19
        self.operation = self.make_operation(monkey_lines[2])
        # Test: divisible by 23
        self.monkey_test_prime = int(monkey_lines[3].split(" by ")[1])
        self.monkey_test = lambda num: num % self.monkey_test_prime == 0
        # If true: throw to monkey 2
        # If false: throw to monkey 3
        self.test_true_target = int(monkey_lines[4].split("monkey ")[1])
        self.test_false_target = int(monkey_lines[5].split("monkey ")[1])

    def make_operation(self, op_line):
        partial_split = op_line.split(" = ")[1]
        lambda_string = "lambda old : " + partial_split
        return eval(lambda_string)


def make_monkey_list(lines):
    monkeys = []
    ptr = 0
    while ptr < len(lines):
        new_monkey_string = []
        while ptr < len(lines) and lines[ptr] != "":
            new_monkey_string.append(lines[ptr])
            ptr += 1
        monkeys.append(Monkey(new_monkey_string))
        ptr += 1
    return monkeys


def solve_pt_1(input_path):
    lines = read_file_with_strip(input_path)
    monkeys = make_monkey_list(lines)
    for round_number in range(20):
        for monkey in monkeys:
            for single_item in monkey.item_list:
                monkey.items_inspected += 1
                new_val = monkey.operation(single_item)
                new_val = floor(new_val / 3)
                if monkey.monkey_test(new_val):
                    monkeys[monkey.test_true_target].item_list.append(new_val)
                else:
                    monkeys[monkey.test_false_target].item_list.append(new_val)
            monkey.item_list = []
    for monkey in monkeys:
        print(monkey.items_inspected)
    print(sorted([x.items_inspected for x in monkeys], reverse=True))
    sorted_item_list = (sorted([x.items_inspected for x in monkeys], reverse=True)[:2])
    print(sorted_item_list[0] * sorted_item_list[1])


def solve_pt_2(input_path):
    lines = read_file_with_strip(input_path)
    monkeys = make_monkey_list(lines)
    globalMod = 1
    for monkey in monkeys:
        globalMod *= monkey.monkey_test_prime
    for round_number in range(10000):
        print(round_number)
        for monkey in monkeys:
            for single_item in monkey.item_list:
                monkey.items_inspected += 1
                new_val = monkey.operation(single_item) % globalMod
                if monkey.monkey_test(new_val):
                    monkeys[monkey.test_true_target].item_list.append(new_val)
                else:
                    monkeys[monkey.test_false_target].item_list.append(new_val)
            monkey.item_list = []
    for monkey in monkeys:
        print(monkey.items_inspected)
    print([x.items_inspected for x in monkeys])
    print(sorted([x.items_inspected for x in monkeys], reverse=True))
    sorted_item_list = (sorted([x.items_inspected for x in monkeys], reverse=True)[:2])
    print(sorted_item_list[0] * sorted_item_list[1])


day = "11"
sample_path = "inputDir/" + day + "_Sample.txt"
data_path = "inputDir/" + day + "_Data.txt"
solve_pt_2(data_path)
