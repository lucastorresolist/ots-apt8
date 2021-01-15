from Back.models.model_categories import Category
from Back.dao_db.dao_base import DaoBase


class DaoCategory(DaoBase):
    def create(self, model: Category) -> None:
        script = f"INSERT INTO categories (name, description) values ('{model.name}','{model.description}')"
        return super().execute(script)

    def read_all(self) -> list:
        list_categories = []
        script = "SELECT id, name, description FROM categories"
        result = super().read(script)
        for item in result:
            category = Category(item[1], item[2], item[0])
            list_categories.append(category)
        return list_categories

    def read_by_id(self, id: int) -> Category:
        category = None
        script = f"SELECT id, name, description FROM categories WHERE id = {id};"
        result = super().read(script)
        if result:
            for item in result:
                category = Category(item[1], item[2], item[0])
        return category

    def delete(self, id: int) -> bool:
        try:
            script = f"DELETE FROM categories WHERE id = {id};"
            super().execute(script)
            return True
        except Exception as e:
            return False

    def update(self, model: Category) -> bool:
        try:
            script = f"UPDATE categories SET name = '{model.name}', description = '{model.description}' \
                WHERE id = {model.id};"
            super().execute(script)
            return True
        except Exception as e:
            return False

    def entity(self):
        return 'Category'
