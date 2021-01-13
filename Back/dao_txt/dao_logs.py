import datetime as datetime
from Back.models.model_logs import Log


root = 'Log/log.txt'

def save_log(log:Log):
    with open(root, 'a') as files:
        data = datetime.datetime.now()
        files.write(data.strftime(
            f"%d/%m/%Y %H:%M:%S | {log.action} | {log.type}\n"))

def list_logs():
    list_log = []
    with open(root, 'r') as file_log:
        for item in file_log:
            temp_log = item.strip().split(' | ')
            temp_log[2] = temp_log[2].strip()
            date = log[0] + '-' + log[1]
            log = Log(item[2], item[3], date)
            list_log.append(log)
    return list_log
