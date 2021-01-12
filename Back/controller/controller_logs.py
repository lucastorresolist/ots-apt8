from Back.dao_db.dao_logs import save_log, list_logs

def save_l(action: str, type:str) -> None:
    save_log(action, type)

def list_l() -> list:
    list_log = list_logs()
    return list_log
