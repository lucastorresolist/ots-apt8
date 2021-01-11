from datetime import datetime
import re

import sys
sys.path.append('.')

from Back.archive import *

import json

import sys
sys.path.append('.')


def save_log(message, type) -> None:
    date = datetime.today().strftime('%d/%m/%Y %H:%M:%S')
    message = f'{date}", "{message}", "{type}"'
    write("../Log/log.txt", message)

def read_log():
    file = open('../Log/log.txt', 'r').readlines()
    lines = []
    for line in file:
        lines.append(json.loads(line))
    return lines


def save_log(message, tag) -> None:
    message = f"[{datetime.today().strftime('%d/%m/%Y %H:%M:%S')}]: {message} - {tag}"
    write("./Log/log.txt", message)

def read_log():
    file = open('./Log/log.txt', 'r').readlines()
    lines = []

    for line in file:
        log_message = line.replace("\n", "")

        tag = re.search("Insert$|List$", line).group()
        
        if tag == "List":
            line = {"message": log_message, "color": "red" }
        elif tag == "Insert":
            line = {"message": log_message, "color": "blue" }

        lines.append(line)
    return lines

