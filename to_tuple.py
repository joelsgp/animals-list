#!/usr/bin python3


with open("lines.txt") as lines_file, open("lines.py", "w") as py_file:
    py_file.write("animals = (\n")
    for line in lines_file.readlines():
        line = line.removesuffix("\n")
        py_file.write(f'    "{line}",\n')
    py_file.write(")\n")
