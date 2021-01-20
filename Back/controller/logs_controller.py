from Back.dao_db.logs_dao import LogDao


class LogController():
    def create(self, model)-> None:
        return LogDao().save(model)

    def read_all(self)-> list:
        return LogDao().read_all()
