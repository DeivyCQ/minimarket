from classes.venta import Venta_cabecera, Venta_detalle
from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu

class Venta_controller:
    def __init__(self):
        self.venta_cabecera = Venta_cabecera()
        self.venta_detalle = Venta_detalle()
        self.salir = False

    def menu(self):
        while True:
            try:
                print('''
                =============
                    Venta
                =============
                ''')
                menu = ['Listar Ventas', 'Buscar Venta', "Nueva Venta", "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_ventas()
                elif respuesta == 2:
                    self.buscar_venta()
                elif respuesta == 3:
                    self.insertar_venta()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def listar_ventas(self):
        print('''
        ======================
            Lista de Venta
        ======================
        ''')
        ventas_cabecera = self.venta_cabecera.obtener_ventas_cabecera('id_venta_cabecera')
        ventas_detalle = self.venta_detalle.obtener_ventas_detalle('id_venta_detalle')
        print(print_table(ventas_cabecera, ['ID', 'Tipo', 'Comprobante', 'Fecha', 'Precio']))
        print(print_table(ventas_detalle, ['ID', 'Posicion', 'ID Producto', 'Descripción', 'Cantidad', 'UM', 'PU', 'Precio Total']))
        input("\nPresione una tecla para continuar...")

    def buscar_venta(self):
        print('''
        ====================
            Buscar Venta
        ====================
        ''')
        try:
            id_venta = input_data("Ingrese el ID de la Venta >> ", "int")
            venta_cabecera = self.venta_cabecera.obtener_ventas_cabecera({'id_venta_cabecera': id_venta})
            venta_detalle = self.venta_detalle.obtener_ventas_detalle({'id_venta_detalle': id_venta})
            print(print_table(ventas_cabecera, ['ID', 'Tipo', 'Comprobante', 'Fecha', 'Precio']))
            print(print_table(ventas_detalle, ['ID', 'Posicion', 'ID Producto', 'Descripción', 'Cantidad', 'UM', 'PU', 'Precio Total']))
            
            if venta_cabecera:
                if pregunta("¿Deseas dar mantenimiento a la Venta?"):
                    opciones = ['Editar Venta', 'Eliminar Venta', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_venta_cabecera(id_venta)
                        self.editar_venta_detalle(id_venta)
                    elif respuesta == 2:
                        self.eliminar_venta_cabecera(id_venta)
                        self.eliminar_venta_detalle(id_venta)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def insertar_venta(self):
        print('''
        ==================================
            Datos de Cabecera de Venta
        ==================================
        ''')        
        tipo = input_data("Ingrese Tipo de Venta >> ")
        comprobante = input_data("Ingrese Comprobante de Venta >> ")
        fecha = input_data("Ingrese Fecha de Venta >> ")
        precio_total = input_data("Ingrese Precio total >> ", "int")
        
        print('''
        =================================
            Datos de Detalle de Venta
        =================================
        ''')
        posicion = input_data("Ingrese Posición >> ", "int")
        id_producto = input_data("Ingrese ID Producto >> ", "int")
        descripcion = input_data("Ingrese del Producto >> ")
        cantidad = input_data("Ingrese del Producto >> ", "int")
        unidad_medida = input_data("Ingrese UM del Producto >> ", "int")
        precio_unitario = input_data("Ingrese Precio Unitario >> ", "int")
        precio_item_total = input_data("Ingrese Precio Total >> ", "int")

        self.venta_cabecera.guardar_venta_cabecera({
            'tipo': tipo,
            'comprobante': comprobante,
            'fecha': fecha,
            'precio': precio_total
        })
        self.venta_detalle.guardar_venta_detalle({
            'posicion': posicion,
            'id_producto': id_producto,
            'descripcion': descripcion,
            'cantidad': cantidad,
            'unidad_medida': unidad_medida,
            'precio_unitario': precio_unitario,
            'precio_total': precio_item_total
        })
        print('''
        =================================
            Nueva Venta agregado !
        =================================
        ''')
        self.listar_ventas()

    def editar_venta(self, id_venta):
        print('''
        =================================
            Datos de Detalle de Venta
        =================================
        ''')
        posicion = input_data("Ingrese Posición >> ", "int")
        id_producto = input_data("Ingrese ID Producto >> ", "int")
        descripcion = input_data("Ingrese del Producto >> ")
        cantidad = input_data("Ingrese del Producto >> ", "int")
        unidad_medida = input_data("Ingrese UM del Producto >> ", "int")
        precio_unitario = input_data("Ingrese Precio Unitario >> ", "int")
        precio_item_total = input_data("Ingrese Precio Total >> ", "int")

        self.venta_detalle.modificar_venta_detalle({
            'id_venta_detalle': id_venta
        }, {
            'posicion': posicion,
            'id_producto': id_producto,
            'descripcion': descripcion,
            'cantidad': cantidad,
            'unidad_medida': unidad_medida,
            'precio_unitario': precio_unitario,
            'precio_total': precio_item_total
        })
        print('''
        ==========================
            Venta editado !
        ==========================
        ''')

    def eliminar_venta(self, id_venta):
        self.venta_cabecera.eliminar_venta_cabecera({
            'id_venta_cabecera': id_venta
        })
        self.venta_detalle.eliminar_venta_detalle({
            'id_venta_detalle': id_venta
        })
        print('''
        =========================
            Venta Eliminado !
        =========================
        ''')