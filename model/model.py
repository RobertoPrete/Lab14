import copy

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

    def getLongestPath(self, sourceId):
        source = self._idMapOrders[int(sourceId)]
        cammino_piu_lungo = []

        tree = nx.dfs_tree(self._graph, source)   # restituisce un albero orientato costruito con una ricerca in profondità (DFS) del grafo a partire da source
        nodi = list(tree.nodes())
        for node in nodi:
            cammino_temporaneo = [node]
            while cammino_temporaneo[0] != source:  # continua finchè il primo nodo del cammino non è il nodo source, cioè finché non si è risaliti fino alla radice dell'albero DFS
                predecessori = nx.predecessor(tree, source, cammino_temporaneo[0])  # trova i predecessori del nodo corrente nel percorso da source fino a quel nodo (cammino_temporaneo[0]).
                                                                                    # La funzione nx.predecessor restituisce una lista di predecessori (di solito uno solo, dato che si tratta di un albero)
                cammino_temporaneo.insert(0, predecessori[0])  # inserisce il predecessore all'inizio del cammino, "risalendo" il percorso verso il nodo source
            if len(cammino_temporaneo) > len(cammino_piu_lungo):
                cammino_piu_lungo = copy.deepcopy(cammino_temporaneo)

        return cammino_piu_lungo

    def getGraphDetails(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()

    def getStores(self):
        return DAO.getStores()

    def getNodes(self):
        return self._nodes
