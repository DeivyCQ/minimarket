from connection.conn import Conexion

class Genero:
    def __init__(self):
        self.model = Conexion('sistema_biblioteca')

    def guardar_lector(self, genero):
        return self.model.insert(periodo)

    def obtener_lector(self, genero_id):
        return self.model.get_by_id(genero_id)

    def obtener_lectores(self, order):
        return self.model.get_all(order)

    def buscar_lectores(self, data_genero):
        return self.model.get_by_column(data_genero)

    def modificar_lector(self, lector_id, data_genero):
        return self.model.update(lector_id, data_genero)

    def eliminar_lector(self, lector_id):
        return self.model.delete(lector_id)