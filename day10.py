from inputReader import read_file_with_strip


class CPU:
    def __init__(self):
        self.current_voltage = 1
        # adding two steps to match cycles from problem
        self.history = [1, 1]
        self.command_history = []

    def process_command(self, line):
        command_split = line.split(" ")
        self.command_history.append([len(self.history), line])
        command = command_split[0]
        if command == "noop":
            self.history.append(self.history[-1])
        elif command == "addx":
            magnitude = int(command_split[1])
            self.history.append(self.history[-1])
            self.history.append(self.history[-1] + magnitude)

    def get_magnitude(self, time):
        return self.history[time] * time


def solve_pt_1(input_path):
    lines = read_file_with_strip(input_path)
    cpu = CPU()
    for line in lines:
        cpu.process_command(line)
    time_list = [20, 60, 100, 140, 180, 220]
    print(sum([cpu.get_magnitude(x) for x in time_list]))
    for x in time_list:
        print(cpu.history[x])


def solve_pt_2(input_path):
    lines = read_file_with_strip(input_path)
    cpu = CPU()
    for line in lines:
        cpu.process_command(line)

    for y in range(0, 6):
        current_line = ""
        for x in range(0, 40):
            # add +1 to match history/cycle
            current_voltage = cpu.history[y * 40 + x + 1]
            volt_range = range(current_voltage - 1, current_voltage + 2)
            # print(y,":",volt_range)
            if x in volt_range:
                current_line += "##"
            else:
                current_line += "  "
        print(current_line)


day = "10"
sample_path = "inputDir/" + day + "_Sample.txt"
data_path = "inputDir/" + day + "_Data.txt"
# solve_pt_1(sample_path)
solve_pt_2(data_path)
