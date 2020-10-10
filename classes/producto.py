from connection.conn import Conexion

class Producto:
    def __init__(self):
        self.model = Conexion('producto')

<<<<<<< HEAD
    def guardar_autor(self, producto):
=======
    def guardar_producto(self, producto):
>>>>>>> a43f2108dfc4ada92d2d283ac884d302ff5ba7ea
        return self.model.insert(producto)

    def obtener_producto(self, id_producto):
        return self.model.get_by_id(id_producto)

    def obtener_productos(self, order):
        return self.model.get_all(order)

<<<<<<< HEAD
    def buscar_producto(self, data_producto):
        return self.model.get_by_column(data_producto)

    def modificar_producto(self, id_autor, data_producto):
=======
    def obtener_productos_inner(self, order):
        return self.model.get_all_inner(fields_select, table_select, order)

    def buscar_producto(self, data_producto):
        return self.model.get_by_column(data_producto)

    def modificar_producto(self, id_producto, data_producto):
>>>>>>> a43f2108dfc4ada92d2d283ac884d302ff5ba7ea
        return self.model.update(id_producto, data_producto)

    def eliminar_producto(self, id_producto):
        return self.model.delete(id_producto)