from classes.tipo_compra import Tipo_compra
from helpers.menu import Menu
from helpers.helper import print_table, input_data, pregunta

class Tipo_compra_controller:
    def __init__(self):
        self.tipo_compra = Tipo_compra()
        self.salir = False
    def menu(self):
        while True:
            try:
                print('''
                ======================
                    Tipo de Compra
                ======================
                ''')
                menu = ['Listar Tipo de Compra', 'Buscar Tipo de Compra', "Nuevo Tipo de Compra", "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_tipo_compra() # Lista las Tipo de Compra de la BD
                elif respuesta == 2:
                    self.buscar_tipo_compra() # Busca Tipo de Compra en base a un ID
                elif respuesta == 3:
                    self.agregar_tipo_compra() # Crea una nuave Tipo de Compra
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def listar_tipo_compra(self):
        print('''
        ===============================
            Lista de Tipo de Compra
        ===============================
        ''')
        tipo_compra = self.tipo_compra.obtener_tipo_compra('id_tipo_compra')
        print(print_table(tipo_compra, ['ID', 'descripción']))
        input("\nPresione una tecla para continuar...")

    def buscar_tipo_compra(self):
        print('''
        =============================
            Buscar Tipo de Compra
        =============================
        ''')
        try:
            id_tipo_compra = input_data("Ingrese el ID de Tipo de Compra >> ", "int")
            tipo_compra = self.tipo_compra.obtener_tipo_compra({'id_tipo_compra': id_tipo_compra})
            print(print_table(tipo_compra, ['ID', 'descripción']))

            if tipo_compra:
                if pregunta("¿Deseas editar Tipo de Compra?"):
                    opciones = ['Editar Tipo de Compra', 'Eliminar Tipo de Compra', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_tipo_compra(id_tipo_compra)
                    elif respuesta == 2:
                        self.eliminar_tipo_compra(id_tipo_compra)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def agregar_tipo_compra(self):
        print('''
        ============================
            Crear Tipo de Compra
        ============================
        ''')
        try:
            descripcion = input_data("Ingrese descripción de Tipo de Compra >> ")
            self.tipo_compra.guardar_tipo_compra({
                'descripcion': descripcion
            })
        except Exception as e:
            print(f'{str(e)}')
        print('''
        =======================================
            Nuevo Tipo de Compra agregado !
        =======================================
        ''')
        self.listar_tipo_compra()

    def editar_tipo_compra(self, id_tipo_compra):
        try:
            descripcion = input_data("Ingrese nueva descripción de Tipo de Compra >> ")
            self.tipo_compra.modificar_tipo_compra({
                'id_tipo_compra': id_tipo_compra
            }, {
                'descripcion': descripcion
            })
        except Exception as e:
            print(f'{str(e)}')
        print('''
        ================================
            Tipo de Compra Editado !
        ================================
        ''')

    def eliminar_tipo_compra(self, id_tipo_compra):
        try:
            self.tipo_compra.eliminar_tipo_compra({
                'id_tipo_compra': id_tipo_compra
            })
        except Exception as e:
            print(f'{str(e)}')
        print('''
        ==================================
            Tipo de Compra Eliminado !
        ==================================
        ''')