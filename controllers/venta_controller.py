from classes.venta import Venta_cabecera, Venta_detalle
from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu

class Venta_controller:
    def __init__(self):
        self.venta = Venta()
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
        =======================
            Lista de Venta
        =======================
        ''')
        ventas = self.producto.obtener_ventas_cabecera_('id_venta_cabecera')
        print(print_table(ventas, ['ID', 'Tipo', 'Comprobante', 'Fecha', 'Precio Total', 'Precio', 'UM Compra', 'UM Venta']))
        input("\nPresione una tecla para continuar...")

    def buscar_venta(self):
        print('''
        ====================
            Buscar Venta
        ====================
        ''')
        try:
            id_venta = input_data("Ingrese el ID del Producto >> ", "int")
            producto = self.producto.obtener_venta({'id_venta': id_venta})
            print(print_table(libros, ['ID', 'Descripción', 'Categoría', 'Marca', 'Stock', 'Precio', 'UM Compra', 'UM Venta']))

            if producto:
                if pregunta("¿Deseas dar mantenimiento al Producto?"):
                    opciones = ['Editar Producto', 'Eliminar Producto', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_venta(id_venta)
                    elif respuesta == 2:
                        self.eliminar_venta(id_venta)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def insertar_venta(self):
        descripcion = input_data("Ingrese descripción del Producto >> ")
        id_categoria = input_data("Ingrese categoría del Producto >> ", "int")
        id_marca = input_data("Ingrese marca del Producto >> ", "int")
        stock = input_data("Ingrese stock inicial del Producto >> ", "float")
        precio = input_data("Ingrese precio del Producto >> ", "float")
        unidad_medida_compra = input_data("Ingrese unidad de medida de compra del Producto >> ")
        unidad_medida_venta = input_data("Ingrese unidad de medida de venta del Producto >> ")
        self.producto.guardar_venta({
            'descripcion': descripcion
            'id_categoria': id_categoria
            'id_marca': id_marca
            'stock': stock
            'precio': precio
            'unidad_medida_compra': unidad_medida_compra
            'unidad_medida_venta': unidad_medida_venta
        })
        print('''
        =================================
            Nuevo Producto agregado !
        =================================
        ''')
        self.listar_ventas()

    def editar_venta(self, id_venta):
        descripcion = input_data("Ingrese nueva descripción del producto >> ")
        id_categoria = input_data("Ingrese nueva categoría del Producto >> ", "int")
        id_marca = input_data("Ingrese nueva marca del Producto >> ", "int")
        stock = input_data("Ingrese nuevo stock inicial del Producto >> ", "float")
        precio = input_data("Ingrese nuevo precio del Producto >> ", "float")
        unidad_medida_compra = input_data("Ingrese nueva unidad de medida de compra del Producto >> ")
        unidad_medida_venta = input_data("Ingrese nueva unidad de medida de venta del Producto >> ")

        self.producto.modificar_venta({
            'id_venta': id_venta
        }, {
            'descripcion': descripcion
            'id_categoria': id_categoria
            'id_marca': id_marca
            'stock': stock
            'precio': precio
            'unidad_medida_compra': unidad_medida_compra
            'unidad_medida_venta': unidad_medida_venta
        })
        print('''
        ==========================
            Producto editado !
        ==========================
        ''')

    def eliminar_venta(self, id_venta):
        self.producto.eliminar_venta({
            'id_venta': id_venta
        })
        print('''
        =========================
            Producto Eliminado !
        =========================
        ''')