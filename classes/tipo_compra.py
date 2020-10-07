from connection.conn import Conexion

class Tipo_compra:
    def __init__(self):
        self.model = Conexion('tipo_compra')

    def guardar_tipo_compra(self, tipo_compra):
        return self.model.insert(tipo_compra)

    def obtener_tipo_compra(self, id_tipo_compra):
        return self.model.get_by_id(id_tipo_compra)

    def obtener_tipo_compras(self, order):
        return self.model.get_all(order)

    def buscar_tipo_compra(self, data_tipo_compra):
        return self.model.get_by_column(data_tipo_compra)

    def modificar_tipo_compra(self, id_tipo_compra, data_tipo_compra):
        return self.model.update(id_tipo_compra, data_tipo_compra)

    def eliminar_tipo_compra(self, id_tipo_compra):
        return self.model.delete(id_tipo_compra)


