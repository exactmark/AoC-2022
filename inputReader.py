from typing import Mapping, MutableMapping, Sequence, Iterable


def read_file_with_strip(path: str):
    return_list = []
    f = open(path, "r")
    for single_line in f:
        return_list.append(str.strip(single_line))
    return return_list


def read_file(path: str):
    return_list = []
    f = open(path, "r")
    for single_line in f:
        return_list.append(single_line)
    return return_list
