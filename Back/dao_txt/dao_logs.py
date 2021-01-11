import datetime as datetime
import sys
sys.path.append('.')

root = 'Log/log.txt'

def save_log(function_name: str, operation_type: str):
    files = open(root, 'a')
    data = datetime.datetime.now()
    files.write(data.strftime(
        f"%d/%m/%Y | %H:%M:%S | {operation_type} | {function_name}\n"))
    files.close()


def list_logs():
    list_log = []
    file_log = open(root, 'r')
    for l in file_log:
        log = l.strip().split('|')
        log[2] = log[2].strip()
        list_log.append(log)
    return list_log
