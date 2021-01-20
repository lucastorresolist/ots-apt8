from .logs_controller import ControllerLog
from ..models.logs_model import Log


class BaseController:
    def __init__(self, dao):
        self.__dao = dao
        self.__log_controller = ControllerLog()

    def create(self, model:object)-> None:
        request = self.__dao.save(model)

        log = Log("Saved", self.__dao.type_model())
        self.__log_controller.save(log)

        return request

    def read_by_id(self,id:int)-> object:
        return self.__dao.read_by_id(id)

    def read_all(self)-> list:
        request = self.__dao.read_all()

        log = Log("Listed", self.__dao.type_model())
        self.__log_controller.save(log)

        return request

    def delete(self, id:int)-> None:
        model = self.read_by_id(id)
        self.__dao.delete(model)

        log = Log("Delete", self.__dao.type_model())
        self.__log_controller.save(log)

    def update(self, model:object)-> None:
        self.__dao.save(model)
        log = Log("Update", self.__dao.type_model())
        self.__log_controller.save(log)


    def update(self, model:object)-> None:
        self.__dao.save(model)

     

