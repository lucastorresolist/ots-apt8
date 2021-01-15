from Back.dao_db.connection import Connection


class DaoBase:
    def execute(self, script: str) -> None:
        with Connection() as conn:
            cursor = conn.cursor()
            cursor.execute(script)
            conn.commit()

    def read(self, script: str) -> tuple:
        with Connection() as conn:
            cursor = conn.cursor()
            cursor.execute(script)
            result = cursor.fetchall()
        return result
