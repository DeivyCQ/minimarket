from classes.marca import Marca
from helpers.menu import Menu
from helpers.helper import print_table, input_data, pregunta

class Marca_controller:
    def __init__(self):
        self.marca = Marca()
        self.salir = False
    def menu(self):
        while True:
            try:
                print('''
                =============================
                    Marca de Producto
                =============================
                ''')
                menu = ['Listar Marca', 'Buscar Marca', "Nueva Marca", "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_marca() # Lista las Marcas de la BD
                elif respuesta == 2:
                    self.buscar_marca() # Busca Marca en base a un ID
                elif respuesta == 3:
                    self.agregar_marca() # Crea una nuave Marca
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def listar_marca(self):
        print('''
        ======================================
            Lista de Marca de Producto
        ======================================
        ''')
        marca = self.marca.obtener_marca('id_marca')
        print(print_table(marca, ['ID', 'descripción']))
        input("\nPresione una tecla para continuar...")

    def buscar_marca(self):
        print('''
        ====================================
            Buscar Marca de Producto
        ====================================
        ''')
        try:
            id_marca = input_data("Ingrese el ID de la Marca >> ", "int")
            marca = self.marca.obtener_marca({'id_marca': id_marca})
            print(print_table(marca, ['ID', 'descripción']))

            if marca:
                if pregunta("¿Deseas editar Marca de producto?"):
                    opciones = ['Editar Marca', 'Eliminar Marca', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_marca(id_marca)
                    elif respuesta == 2:
                        self.eliminar_marca(id_marca)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def agregar_marca(self):
        print('''
        ===============================
            Crear Marca de Producto
        ===============================
        ''')
        try:
            descripcion = input_data("Ingrese descripción de la Marca >> ")
            self.marca.guardar_marca({
                'descripcion': descripcion
            })
        except Exception as e:
            print(f'{str(e)}')
        print('''
        ==============================================
            Nueva Marca de Producto agregado !
        ==============================================
        ''')
        self.listar_marca()

    def editar_marca(self, id_marca):
        try:
            descripcion = input_data("Ingrese nueva descripción de la Marca de producto >> ")
            self.marca.modificar_marca({
                'id_marca': id_marca
            }, {
                'descripcion': descripcion
            })
        except Exception as e:
            print(f'{str(e)}')
        print('''
        =======================================
            Marca de Producto Editado !
        =======================================
        ''')

    def eliminar_marca(self, id_marca):
        try:
            self.marca.eliminar_marca({
                'id_marca': id_marca
            })
        except Exception as e:
            print(f'{str(e)}')
        print('''
        ====================================
            Marca de Producto Eliminado !
        ====================================
        ''')