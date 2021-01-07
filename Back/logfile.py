from datetime import datetime
from Back.archive import *

import json

import sys
sys.path.append('.')


def save_log(message, type) -> None:
    date = datetime.today().strftime('%d/%m/%Y %H:%M:%S')
    message =  "{" + f'"date": "{date}", "message": "{message}", "type": "{type}"' + "}"
    write("../Log/log.txt", message)

def read_log():
    file = open('../Log/log.txt', 'r').readlines()
    lines = []
    for line in file:
        lines.append(json.loads(line))
    return lines

