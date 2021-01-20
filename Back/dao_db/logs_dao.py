from .base_dao import BaseDao
from Back.models.logs_model import Log


class LogDao(BaseDao):
    def __init__(self):
        super().__init__(Log)
