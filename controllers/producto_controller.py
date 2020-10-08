from classes.producto import Producto
from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu


class Producto_controller:
    def __init__(self):
        self.producto = Producto()
        self.salir = False

    def menu(self):
        while True:
            try:
                print('''
                ================
                    Producto
                ================
                ''')
                menu = ['Listar Producto', 'Buscar Producto', "Nuevo Producto", "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_productos()
                elif respuesta == 2:
                    self.buscar_producto()
                elif respuesta == 3:
                    self.insertar_producto()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def listar_productos(self):
        print('''
        ==========================
            Lista de Productos
        ==========================
        ''')
        libros = self.producto.obtener_productos_inner('id_producto')
        print(print_table(libros, ['ID', 'Descripción', 'Categoría', 'Marca', 'Stock', 'Precio', 'UM Compra', 'UM Venta']))
        input("\nPresione una tecla para continuar...")

    def buscar_producto(self):
        print('''
        =======================
            Buscar Producto
        =======================
        ''')
        try:
            id_producto = input_data("Ingrese el ID del Producto >> ", "int")
            producto = self.producto.obtener_producto({'id_producto': id_producto})
            print(print_table(libros, ['ID', 'Descripción', 'Categoría', 'Marca', 'Stock', 'Precio', 'UM Compra', 'UM Venta']))

            if producto:
                if pregunta("¿Deseas dar mantenimiento al Producto?"):
                    opciones = ['Editar Producto', 'Eliminar Producto', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_producto(id_producto)
                    elif respuesta == 2:
                        self.eliminar_producto(id_producto)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def insertar_producto(self):
        descripcion = input_data("Ingrese descripción del Producto >> ")
        id_categoria = input_data("Ingrese categoría del Producto >> ", "int")
        id_marca = input_data("Ingrese marca del Producto >> ", "int")
        stock = input_data("Ingrese stock inicial del Producto >> ", "float")
        precio = input_data("Ingrese precio del Producto >> ", "float")
        unidad_medida_compra = input_data("Ingrese unidad de medida de compra del Producto >> ")
        unidad_medida_venta = input_data("Ingrese unidad de medida de venta del Producto >> ")
        self.producto.guardar_producto({
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
        self.listar_productos()

    def editar_producto(self, id_producto):
        descripcion = input_data("Ingrese nueva descripción del producto >> ")
        id_categoria = input_data("Ingrese nueva categoría del Producto >> ", "int")
        id_marca = input_data("Ingrese nueva marca del Producto >> ", "int")
        stock = input_data("Ingrese nuevo stock inicial del Producto >> ", "float")
        precio = input_data("Ingrese nuevo precio del Producto >> ", "float")
        unidad_medida_compra = input_data("Ingrese nueva unidad de medida de compra del Producto >> ")
        unidad_medida_venta = input_data("Ingrese nueva unidad de medida de venta del Producto >> ")

        self.producto.modificar_producto({
            'id_producto': id_producto
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

    def eliminar_producto(self, id_producto):
        self.producto.eliminar_producto({
            'id_producto': id_producto
        })
        print('''
        =========================
            Producto Eliminado !
        =========================
        ''')