import sys
sys.path.append('.')

from Back.archive import *

file_route = '../Data/category.txt'


def create_category(name: str, description: str) -> None:
    file.open(file_route, 'a')
    file.write(f'{name};{description}\n')
    file.close()
    action = f'Category {name} successfully created!'
    write(action)



