from inputReader import read_file

class Elf:
    def __init__(self):
        self.bag = []

    def add_to_bag(self,item:int):
        self.bag.append(item)

    def get_bag_weight(self):
        return sum(self.bag)

def get_elf_list(input_lines):
    elf_list = []
    this_elf = Elf()
    for x in input_lines:
        if x == "":
            elf_list.append(this_elf)
            this_elf = Elf()
        else:
            this_elf.add_to_bag(int(x))
    elf_list.append(this_elf)
    return elf_list

def solve_pt_1(input_path):
    input_lines = read_file(input_path)
    elf_list = get_elf_list(input_lines)
    max_bag = 0
    for e in elf_list:
        if e.get_bag_weight() > max_bag:
            max_bag = e.get_bag_weight()
    print(max_bag)

def solve_pt_2(input_path):
    input_lines = read_file(input_path)
    elf_list = get_elf_list(input_lines)
    elf_list.sort(key=lambda x:x.get_bag_weight(),reverse=True)
    for x in elf_list:
        print(x.get_bag_weight())
    print(sum([x.get_bag_weight() for x in elf_list[:3]]))


sample_path = "inputDir/01_Sample.txt"
data_path = "inputDir/01_Data.txt"
solve_pt_2(data_path)
