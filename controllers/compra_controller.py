from classes.compra import Compra
from helpers.menu import Menu
from helpers.helper import print_table, input_data, pregunta

class Compra_controller:
    def __init__(self):
        self.compra = Compra()
        self.salir = False
    def menu(self):
        while True:
            try:
                print('''
                =============================
                    Compras
                =============================
                ''')
                menu = ['Listar Compras', 'Buscar Compra', "Nueva Compra", "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_compra() # Lista los roles de la BD
                elif respuesta == 2:
                    self.buscar_compra() # Busca Rol en base a un ID
                elif respuesta == 3:
                    self.agregar_compra() # Crea un nuevo Rol
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def listar_compra(self):
        print('''
        ======================================
            Lista de Compras
        ======================================
        ''')
        compras = self.compra.obtener_compras('id')
        print(print_table(compras, ['ID', 'Descripción de compra']))
        input("\nPresione una tecla para continuar...")

    def buscar_compra(self):
        print('''
        ====================================
            Buscar Compra
        ====================================
        ''')
        try:
            id_compra = input_data("Ingrese el ID de la compra >> ", "int")
            compra = self.compra.obtener_compra({'id_compra': id_compra})
            print(print_table(compra, ['ID', 'descripción']))

            if compra:
                if pregunta("¿Deseas editar Compra?"):
                    opciones = ['Editar Compra', 'Eliminar Compra', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_compra(id_compra)
                    elif respuesta == 2:
                        self.eliminar_compra(id_compra)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def agregar_compra(self):
        print('''
        ===============================
            Crear Compra
        ===============================
        ''')
        try:
            descripcion = input_data("Ingrese descripción de la Compra  |otros campos>> ")
            self.compra.guardar_compra({
                'descripcion': descripcion
            })
        except Exception as e:
            print(f'{str(e)}')
        print('''
        ==============================================
            Nueva compra registrada !
        ==============================================
        ''')
        self.listar_compra()

    def editar_compra(self, id_compra):
        try:
            descripcion = input_data("Ingrese nueva descripción de la Compra >> ")
            self.compra.modificar_compra({
                'id_compra': id_compra
            }, {
                'descripcion': descripcion
            })
        except Exception as e:
            print(f'{str(e)}')
        print('''
        =======================================
            Compra Editada !
        =======================================
        ''')

    def eliminar_compra(self, id_compra):
        try:
            self.compra.eliminar_compra({
                'id_compra': id_compra
            })
        except Exception as e:
            print(f'{str(e)}')
        print('''
        ====================================
           Compra Eliminada !
        ====================================
        ''')