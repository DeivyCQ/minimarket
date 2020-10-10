from connection.conn import Conexion

class Stock:
    def __init__(self):
        self.model = Conexion('stock')

    def guardar_stock(self, stock):
        return self.model.insert(stock)

    def obtener_stock(self, id_stock):
        return self.model.get_by_id(id_stock)

    def obtener_stocks(self, order):
        return self.model.get_all(order)

    def buscar_stock(self, data_stock):
        return self.model.get_by_column(data_stock)

    def modificar_stock(self, id_autor, data_stock):
        return self.model.update(id_autor, data_stock)

    def eliminar_stock(self, id_stock):
        return self.model.delete(id_stock)