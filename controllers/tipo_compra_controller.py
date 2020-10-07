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
                =============================
                    Tipo de compra
                =============================
                ''')
                menu = ['Listar Tipos de compra', 'Buscar Tipo de compra', "Nuevo Tipo de compra", "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_tipo_compra() # Lista los roles de la BD
                elif respuesta == 2:
                    self.buscar_tipo_compra() # Busca Rol en base a un ID
                elif respuesta == 3:
                    self.agregar_tipo_compra() # Crea un nuevo Rol
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def listar_tipo_compra(self):
        print('''
        ======================================
            Lista de Tipos de compra
        ======================================
        ''')
        tipo_compra = self.tipo_compra.obtener_tipo_compras('id_tipo_compra')
        print(print_table(tipo_compra, ['ID', 'descripción']))
        input("\nPresione una tecla para continuar...")

    def buscar_tipo_compra(self):
        print('''
        ====================================
            Buscar Rol de Usuario
        ====================================
        ''')
        try:
            id_tipo_compra = input_data("Ingrese el ID del Tipo de compra >> ", "int")
            tipo_compra = self.tipo_compra.obtener_tipo_compra({'id_tipo_compra': id_tipo_compra})
            print(print_table(tipo_compra, ['ID', 'descripción']))

            if tipo_compra:
                if pregunta("¿Deseas editar Tipo de compra?"):
                    opciones = ['Editar Tipo de compra', 'Eliminar Tipo de compra', 'Salir']
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
        ===============================
            Crear Tipo de compra
        ===============================
        ''')
        try:
            descripcion = input_data("Ingrese descripción del Tipo de compra >> ")
            self.tipo_compra.guardar_tipo_compra({
                'descripcion': descripcion
            })
        except Exception as e:
            print(f'{str(e)}')
        print('''
        ==============================================
            Nuevo Tipo de compra agregado !
        ==============================================
        ''')
        self.listar_tipo_compra()

    def editar_tipo_compra(self, id_tipo_compra):
        try:
            descripcion = input_data("Ingrese nueva descripción del Tipo de compra >> ")
            self.tipo_compra.modificar_tipo_compra({
                'id_tipo_compra': id_tipo_compra
            }, {
                'descripcion': descripcion
            })
        except Exception as e:
            print(f'{str(e)}')
        print('''
        =======================================
            Tipo de compra Editado !
        =======================================
        ''')

    def eliminar_tipo_compra(self, id_tipo_compra):
        try:
            self.tipo_compra.eliminar_tipo_compra({
                'id_tipo_compra': id_tipo_compra
            })
        except Exception as e:
            print(f'{str(e)}')
        print('''
        ====================================
           Tipo de compra Eliminado !
        ====================================
        ''')