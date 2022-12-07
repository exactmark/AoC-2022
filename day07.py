from inputReader import read_file_with_strip


class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        if not parent:
            self.abs_path = name
        else:
            self.abs_path = parent.abs_path + "/" + name
        self.parent = parent
        self.files = {}
        self.child_dirs = {}
        self.has_been_polled = False

    def add_dir(self, child):
        new_dir = Directory(child, self)
        self.child_dirs[child] = new_dir
        return new_dir

    def add_file(self, file_line):
        split_line = file_line.split(" ")
        self.files[split_line[1]] = int(split_line[0])

    def get_size(self):
        return sum(self.files.values()) + sum([child.get_size() for child in self.child_dirs.values()])


class Filesystem:
    def __init__(self):
        # self.working_dir_path = "/"
        self.working_dir = Directory("/")
        self.full_dir_map = {self.working_dir.abs_path: self.working_dir}
        self.home = self.working_dir

    def parse_input_from(self, lines, ptr):
        command = lines[ptr]
        if command[0] != "$":
            raise Exception("not a command")
        if command.split(" ")[1] == "ls":
            return self.process_list_dir(lines, ptr)
        self.process_dir_change(command)
        return ptr + 1

    def process_dir_change(self, command):
        target = command.split(" ")[2]
        if target == "/":
            self.working_dir = self.home
            return
        if target == "..":
            self.working_dir = self.working_dir.parent
            return
        self.working_dir = self.working_dir.child_dirs[target]

    def process_list_dir(self, lines, ptr):
        # ptr is at $ ls
        ptr += 1
        if self.working_dir.has_been_polled:
            while lines[ptr][0] != "$":
                ptr += 1
                if ptr >= len(lines):
                    return ptr
            return ptr
        self.working_dir.has_been_polled = True
        while lines[ptr][0] != "$":
            if lines[ptr][0] == "d":
                new_dir = self.working_dir.add_dir(lines[ptr].split(" ")[1])
                self.full_dir_map[new_dir.abs_path] = new_dir
            else:
                self.working_dir.add_file(lines[ptr])
            ptr += 1
            if ptr >= len(lines):
                return ptr
        return ptr


def solve_pt_1(input_path):
    lines = read_file_with_strip(input_path)
    ptr = 0
    file_system = Filesystem()
    while ptr < len(lines):
        # print(file_system.full_dir_map)
        # print([x for x in file_system.full_dir_map.keys()])
        ptr = file_system.parse_input_from(lines, ptr)
    print("read done")
    end_sum = 0
    for dir in file_system.full_dir_map.keys():
        this_size = file_system.full_dir_map[dir].get_size()
        # print(dir ," : ",this_size)
        if this_size < 100000:
            end_sum += this_size
    print(end_sum)


def solve_pt_2(input_path):
    lines = read_file_with_strip(input_path)
    ptr = 0
    file_system = Filesystem()
    while ptr < len(lines):
        # print(file_system.full_dir_map)
        # print([x for x in file_system.full_dir_map.keys()])
        ptr = file_system.parse_input_from(lines, ptr)
    print("read done")
    total_space = 70000000
    required = 30000000
    current_free = total_space - file_system.home.get_size()
    print("current_free:", current_free)
    target_size = required - current_free
    print("target_size:", target_size)
    current_best = file_system.home
    for single_dir in file_system.full_dir_map.keys():
        this_size = file_system.full_dir_map[single_dir].get_size()
        # print("dir:", single_dir, ":", this_size)
        if this_size > target_size:
            if this_size < current_best.get_size():
                current_best = file_system.full_dir_map[single_dir]
    print(current_best.get_size())


day = "07"
sample_path = "inputDir/" + day + "_Sample.txt"
data_path = "inputDir/" + day + "_Data.txt"
# solve_pt_1(data_path)
solve_pt_2(data_path)
