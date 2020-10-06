from connection.conn import Conexion

class Categoria:
    def __init__(self):
        self.model = Conexion('categoria')

    def guardar_categoria(self, categoria):
        return self.model.insert(categoria)

    def obtener_categoria(self, id_categoria):
        return self.model.get_by_id(id_categoria)

    def obtener_categoriaes(self, order):
        return self.model.get_all(order)

    def buscar_categoria(self, data_categoria):
        return self.model.get_by_column(data_categoria)

    def modificar_categoria(self, id_categoria, data_categoria):
        return self.model.update(id_categoria, data_categoria)

    def eliminar_categoria(self, id_categoria):
        return self.model.delete(id_categoria)


