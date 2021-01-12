from Back.models.log import Log
from Back.dao_db.dao_logs import save_log, list_logs


def save_l(log: Log) -> None:
    save_log(log)


def list_l() -> list:
    list_log = list_logs()
    return list_log
