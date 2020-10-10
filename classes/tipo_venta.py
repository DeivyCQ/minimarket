from connection.conn import Conexion

class Tipo_venta:
    def __init__(self):
        self.model = Conexion('tipo_venta')

    def guardar_autor(self, tipo_venta):
        return self.model.insert(tipo_venta)

    def obtener_tipo_venta(self, id_tipo_venta):
        return self.model.get_by_id(id_tipo_venta)

    def obtener_tipo_ventas(self, order):
        return self.model.get_all(order)

    def buscar_tipo_venta(self, data_tipo_venta):
        return self.model.get_by_column(data_tipo_venta)

    def modificar_tipo_venta(self, id_tipo_venta, data_tipo_venta):
        return self.model.update(id_tipo_venta, data_tipo_venta)

    def eliminar_tipo_venta(self, id_tipo_ventar):
        return self.model.delete(id_tipo_venta)