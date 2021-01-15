from Back.controller.controller_logs import ControllerLog
from Back.models.model_logs import Log


class ControllerBase:
    def __init__(self, dao):
        self.__dao = dao

    def create(self, model:object)-> None:
        request = self.__dao.create(model)
        log = Log("Saved", self.__dao.entity())
        ControllerLog().create(log)
        return request

    def read_by_id(self,id:int)-> object:
        return self.__dao.read_by_id(id)

    def read_all(self)-> list:
        request = self.__dao.read_all()
        log = Log("Listed", self.__dao.entity())
        ControllerLog().create(log)
        return request

    def delete(self, id:int)-> None:
        log = Log("Delete", self.__dao.entity())
        ControllerLog().create(log)
        self.__dao.delete(id)

    def update(self, model:object)-> None:
        log = Log("Update", self.__dao.entity())
        ControllerLog().create(log)
        self.__dao.update(model)
