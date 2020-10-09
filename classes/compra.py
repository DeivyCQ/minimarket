from connection.conn import Conexion

class Compra:
    def __init__(self):
        self.model = Conexion('compra')

    def guardar_compra(self, compra):
        return self.model.insert(compra)

    def obtener_compra(self, id_compra):
        return self.model.get_by_id(id_compra)

    def obtener_compras(self, order):
        return self.model.get_all(order)

    def buscar_compra(self, data_compra):
        return self.model.get_by_column(data_compra)

    def modificar_compra(self, id_compra, data_compra):
        return self.model.update(id_compra, data_compra)

    def eliminar_compra(self, id_compra):
        return self.model.delete(id_compra)


