from .dao_base import DaoBase
from Back.models.model_marketplaces import Marketplace


class MarketplaceDao(DaoBase):
    def create(self, model:Marketplace)-> None:
        query = f"""INSERT INTO marketplaces 
                    (name, description) 
                    VALUES 
                    ('{model.name}','{model.description}');"""
        super().execute(query)

    def read_by_id(self, id:int)-> Marketplace:
        query = f"""SELECT name, description, id FROM marketplaces WHERE id={id};"""
        result = super().read(query)[0]
        marketplace = Marketplace(result[0], result[1], result[2])
        return marketplace

    def read_all(self)-> list:
        marketplaces = []
        query = f"""SELECT name, description, id FROM marketplaces;"""
        list_result = super().read(query)
        for result in list_result:
            marketplace = Marketplace(result[0], result[1], result[2])
            marketplaces.append(marketplace)
        return marketplaces
        
    def delete(self, id:int)-> None:
        query = f"""DELETE FROM marketplaces WHERE id={id};"""
        super().execute(query)
    
    def update(self, model:Marketplace)-> None:
        query = f"""UPDATE marketplaces 
                    SET
                        name = '{model.name}', 
                        description = '{model.description}'
                    WHERE id = {model.id};"""
        super().execute(query)
