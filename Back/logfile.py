from datetime import datetime
from archive import *


def save_log(message) -> None:
    message = f"[{datetime.today().strftime('%d/%m/%Y %H:%M:%S')}]: {message}\n"
    write("../Log/log.txt", message)
