from database.DB_connect import DBConnect
from model.store import Store


class DAO:
    def __init__(self):
        pass

    @staticmethod
    def getStores():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = "select * from stores s "
        cursor.execute(query)
        for row in cursor:
            result.append(Store(**row))
        cursor.close()
        conn.close()
        return result


if __name__ == "__main__":
    print(DAO.getStores())

