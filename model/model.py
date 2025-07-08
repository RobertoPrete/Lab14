import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.DiGraph()
        self._nodes = None
        self._edges = None

        self._orders = DAO.getAllOrders()
        self._idMapOrders = {}
        for order in self._orders:
            self._idMapOrders[order.order_id] = order

    def buildGraph(self, store, numGiorniMax):
        self._graph.clear()
        self._nodes = DAO.getAllNodes(store)
        self._graph.add_nodes_from(self._nodes)
        self._edges = DAO.getAllEdges(store, numGiorniMax, self._idMapOrders)
        for edge in self._edges:
            self._graph.add_edge(edge.o1, edge.o2, weight=edge.peso)




    def getGraphDetails(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()

    def getStores(self):
        return DAO.getStores()

    def getNodes(self):
        return self._nodes
