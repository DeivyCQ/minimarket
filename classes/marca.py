from connection.conn import Conexion

class Marca:
    def __init__(self):
        self.model = Conexion('marca')

    def guardar_marca(self, marca):
        return self.model.insert(marca)

    def obtener_marca(self, id_marca):
        return self.model.get_by_id(id_marca)

    def obtener_marcas(self, order):
        return self.model.get_all(order)

    def buscar_marca(self, data_marca):
        return self.model.get_by_column(data_marca)

    def modificar_marca(self, id_marca, data_marca):
        return self.model.update(id_marca, data_marca)

    def eliminar_marca(self, id_marca):
        return self.model.delete(id_marca)


