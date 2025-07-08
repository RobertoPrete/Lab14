import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._store = None

    def fillDD(self):
        stores = self._model.getStores()
        for store in stores:
            self._view._ddStore.options.append(ft.dropdown.Option(text=store, data=store, on_click=self.readDDStore))
        self._view.update_page()

    def readDDStore(self, e):
        self._store = e.control.data

    def handleCreaGrafo(self, e):
        pass

    def handleCerca(self, e):
        pass

    def handleRicorsione(self, e):
        pass
