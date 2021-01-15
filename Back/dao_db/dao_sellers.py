from .dao_base import DaoBase
from Back.models.model_sellers import Seller


class SellerDao(DaoBase):
    def create(self, model:Seller)-> None:
        query = f"""INSERT INTO sellers 
                    (name, phone, email) 
                    VALUES 
                    ('{model.name}','{model.phone}','{model.email}');"""
        super().execute(query)

    def read_by_id(self, id:int)-> Seller:
        query = f"""SELECT name, phone, email, id FROM sellers WHERE id={id};"""
        result = super().read(query)[0]
        seller = Seller(result[0], result[1], result[2], result[3])
        return seller

    def read_all(self)-> list:
        sellers = []
        query = f"""SELECT name, phone, email, id FROM sellers;"""
        list_result = super().read(query)
        for result in list_result:
            seller = Seller(result[0], result[1], result[2], result[3])
            sellers.append(seller)
        return sellers

    def delete(self, id:int)-> None:
        query = f"""DELETE FROM sellers WHERE id={id};"""
        super().execute(query)

    def update(self, model:Seller)-> None:
        query = f"""UPDATE sellers 
                    SET
                        name = '{model.name}', 
                        phone = '{model.phone}', 
                        email = '{model.email}'
                    WHERE id = {model.id};"""
        super().execute(query)

    def entity(self):
        return 'Seller'
