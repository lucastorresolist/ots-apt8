from datetime import datetime
from Back.archive import *


def save_log(message) -> None:
    message = f"[{datetime.today().strftime('%d/%m/%Y %H:%M:%S')}]: {message}\n"
    write("f:\projetos\olistprojetos\marketplacesduplas\marketplace-dupla2\ots-apt9\Log\log.txt", message)
