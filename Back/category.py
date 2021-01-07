import sys
sys.path.append('.')

from Back.archive import *

file_route = '../Data/category.txt'


def create_category(name: str, description: str) -> None:
    file = open(file_route, 'a')
    file.write(f'{name};{description}\n')
    file.close()
    line = f'Category {name} successfully created!'
    write(line)


def list_category(path) -> list:
    file_lines = []
    file = open(path, 'r')
    for line in file.readlines():
        clear_line = line.strip().split(';')
        formated_line = {'name': clear_line[0], 'descriprion': clear_line[1]}
        file_lines.append(formated_line)
    file.close()
    return file_lines
