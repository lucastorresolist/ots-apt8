from Back.dao_db.dao_base import DaoBase
from Back.models.model_logs import Log


class DaoLog(DaoBase):
    def create(self, log: Log) -> None:
        script = f"INSERT INTO logs (action, type) VALUES ('{log.action}','{log.type}')"
        return super().execute(script)

    def read_all(self) -> list:
        list_logs = []
        script = "SELECT id, data, action, type FROM logs"
        result = super().read(script)
        for item in result:
            log = Log(item[2], item[3], item[1], item[0])
            list_logs.append(log)
        return list_logs
