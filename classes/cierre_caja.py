from connection.conn import Conexion

class Cierre_caja:
    def __init__(self):
        self.model = Conexion('cierre_caja')

    def guardar_cierre_caja(self, cierre_caja):
        return self.model.insert(cierre_caja)

    def obtener_cierre_caja(self, id_cierre_caja):
        return self.model.get_by_id(id_cierre_caja)

    def obtener_cierre_cajas(self, order):
        return self.model.get_all(order)

    def buscar_cierre_caja(self, data_cierre_caja):
        return self.model.get_by_column(data_cierre_caja)

    def modificar_cierre_caja(self, id_cierre_caja, data_cierre_caja):
        return self.model.update(id_cierre_caja, data_cierre_caja)

    def eliminar_cierre_caja(self, id_cierre_caja):
        return self.model.delete(id_cierre_caja)