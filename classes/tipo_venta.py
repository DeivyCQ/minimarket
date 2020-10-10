from connection.conn import Conexion

class Tipo_venta:
    def __init__(self):
        self.model = Conexion('tipo_venta')

<<<<<<< HEAD
    def guardar_autor(self, tipo_venta):
=======
    def guardar_tipo_venta(self, tipo_venta):
>>>>>>> a43f2108dfc4ada92d2d283ac884d302ff5ba7ea
        return self.model.insert(tipo_venta)

    def obtener_tipo_venta(self, id_tipo_venta):
        return self.model.get_by_id(id_tipo_venta)

<<<<<<< HEAD
    def obtener_tipo_ventas(self, order):
=======
    def obtener_tipos_venta(self, order):
>>>>>>> a43f2108dfc4ada92d2d283ac884d302ff5ba7ea
        return self.model.get_all(order)

    def buscar_tipo_venta(self, data_tipo_venta):
        return self.model.get_by_column(data_tipo_venta)

    def modificar_tipo_venta(self, id_tipo_venta, data_tipo_venta):
        return self.model.update(id_tipo_venta, data_tipo_venta)

<<<<<<< HEAD
    def eliminar_tipo_venta(self, id_tipo_ventar):
=======
    def eliminar_tipo_venta(self, id_tipo_venta):
>>>>>>> a43f2108dfc4ada92d2d283ac884d302ff5ba7ea
        return self.model.delete(id_tipo_venta)