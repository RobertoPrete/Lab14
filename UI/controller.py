import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._store = None
        self._numGiorniMax = None
        self._node = None

    def fillDD(self):
        stores = self._model.getStores()
        for store in stores:
            self._view._ddStore.options.append(ft.dropdown.Option(text=store.store_id, data=store, on_click=self.readDDStore))
        self._view.update_page()

    def readDDStore(self, e):
        self._store = e.control.data

    def handleCreaGrafo(self, e):
        try:
            self._numGiorniMax = int(self._view._txtIntK.value)
            if self._numGiorniMax is None or self._numGiorniMax == "":
                self._view.controls.clear()
                self._view.controls.append(ft.Text("Inserire il numero massimo di giorni"))
                self._view.update_page()
                return
        except ValueError:
            self._view.controls.clear()
            self._view.controls.append(ft.Text("Inserire il numero massimo di giorni"))
            self._view.update_page()

        self._model.buildGraph(self._store.store_id, self._numGiorniMax)
        self.fillDDNode()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato: "))
        numero_nodi, numero_archi = self._model.getGraphDetails()
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi: {numero_nodi}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di archi: {numero_archi}"))
        self._view.update_page()

    def fillDDNode(self):
        nodes = self._model.getNodes()
        for node in nodes:
            self._view._ddNode.options.append(
                ft.dropdown.Option(text=node.order_id, data=node, on_click=self.readDDNode))
        self._view.update_page()

    def readDDNode(self, e):
        self._node = e.control.data

    def handleCerca(self, e):
        self._view.txt_result.controls.append(ft.Text(f"Nodo di partenza: {self._node.order_id}"))
        self._view.update_page()

    def handleRicorsione(self, e):
        pass
