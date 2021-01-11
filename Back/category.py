import sys
sys.path.append('.')


def list_category(path) -> list:
    file_lines = []
    file = open(path, 'r')
    for line in file.readlines():
        clear_line = line.strip().split(';')
        formated_line = {'name': clear_line[0], 'description': clear_line[1]}
        file_lines.append(formated_line)
    file.close()
    return file_lines
