from connection.conn import Conexion

class Rol:
    def __init__(self):
        self.model = Conexion('rol')

    def guardar_rol(self, rol):
        return self.model.insert(rol)

    def obtener_rol(self, id_rol):
        return self.model.get_by_id(id_rol)

    def obtener_rols(self, order):
        return self.model.get_all(order)

    def buscar_rol(self, data_rol):
        return self.model.get_by_column(data_rol)

    def modificar_rol(self, id_rol, data_rol):
        return self.model.update(id_rol, data_rol)

    def eliminar_rol(self, id_rol):
        return self.model.delete(id_rol)


