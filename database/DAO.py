from database.DB_connect import DBConnect
from model.arco import Arco
from model.order import Order
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

    @staticmethod
    def getAllOrders():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = "select * from orders o"
        cursor.execute(query)
        for row in cursor:
            result.append(Order(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllNodes(store):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """select o.*
                    from orders o, stores s 
                    where o.store_id = s.store_id
                    and o.store_id = %s"""
        cursor.execute(query, (store, ))
        for row in cursor:
            result.append(Order(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges(store, numGiorniMax, idMapOrders):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """Select DISTINCT o1.order_id as o1, o2.order_id as o2, count(oi.quantity+ oi2.quantity) as peso
                    from orders o1, orders o2, order_items oi, order_items oi2 
                    where o1.store_id=%s
                    and o1.store_id=o2.store_id 
                    and o1.order_date > o2.order_date
                    and oi.order_id = o1.order_id
                    and oi2.order_id  = o2.order_id
                    and DATEDIFF(o1.order_Date, o2.order_date) < %s
                    group by o1.order_id, o2.order_id	"""
        cursor.execute(query, (store, numGiorniMax, ))
        for row in cursor:
            result.append(Arco(idMapOrders[row["o1"]], idMapOrders[row["o2"]], row["peso"]))
        cursor.close()
        conn.close()
        return result


if __name__ == "__main__":
    print(DAO.getStores())

