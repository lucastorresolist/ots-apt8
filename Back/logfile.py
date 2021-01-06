from datetime import datetime
from archive import *


def save_log(message) -> None:
    message = f"[{datetime.today().strftime('%d/%m/%Y %H:%M:%S')}]: {message}\n"
    write("../Log/log.txt", message)


def list_marketplaces() -> list:
    file_lines = []
    file = open(save_log, 'a')
    for line in file:
        clear_line = line.strip()
        per_line = clear_line.split(';')
        formated_line = f"{per_line[0], per_line[1]}"
        file_lines.append(formated_line)
    file.close()
    return file_lines
