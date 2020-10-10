from connection.conn import Conexion

class Venta_cabecera:
    def __init__(self):
        self.model = Conexion('venta_cabecera')

    def guardar_venta_cabecera(self, venta_cabecera):
        return self.model.insert(venta_cabecera)

    def obtener_venta_cabecera(self, id_venta_cabecera):
        return self.model.get_by_id(id_venta_cabecera)

    def obtener_ventas_cabecera(self, order):
        return self.model.get_all(order)

    def obtener_ventas_cabecera_inner(self, order):
        return self.model.get_all_inner(fields_select, table_select, order)

    def buscar_venta_cabecera(self, data_venta_cabecera):
        return self.model.get_by_column(data_venta_cabecera)

    def modificar_venta_cabecera(self, id_venta_cabecera, data_venta_cabecera):
        return self.model.update(id_venta_cabecera, data_venta_cabecera)

    def eliminar_venta_cabecera(self, id_venta_cabecera):
        return self.model.delete(id_venta_cabecera)

class Venta_detalle:
    def __init__(self):
        self.model = Conexion('venta_detalle')

    def guardar_venta_detalle(self, venta_detalle):
        return self.model.insert(venta_detalle)

    def obtener_venta_detalle(self, id_venta_detalle):
        return self.model.get_by_id(id_venta_detalle)

    def obtener_ventas_detalle(self, order):
        return self.model.get_all(order)

    def obtener_ventas_detalle_inner(self, order):
        return self.model.get_all_inner(fields_select, table_select, order)

    def buscar_venta_detalle(self, data_venta_detalle):
        return self.model.get_by_column(data_venta_detalle)

    def modificar_venta_detalle(self, id_venta_detalle, data_venta_detalle):
        return self.model.update(id_venta_detalle, data_venta_detalle)

    def eliminar_venta_detalle(self, id_venta_detalle):
        return self.model.delete(id_venta_detalle)