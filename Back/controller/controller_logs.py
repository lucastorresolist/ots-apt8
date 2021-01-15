from Back.dao_db.dao_logs import DaoLog


class ControllerLog():
    def create(self, model)-> None:
        return DaoLog().create(model)

    def read_all(self)-> list:
        return DaoLog().read_all()
