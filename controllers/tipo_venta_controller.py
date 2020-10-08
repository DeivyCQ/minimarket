from classes.tipo_venta import Tipo_venta
from helpers.menu import Menu
from helpers.helper import print_table, input_data, pregunta

class Tipo_venta_controller:
    def __init__(self):
        self.tipo_venta = Tipo_venta()
        self.salir = False
    def menu(self):
        while True:
            try:
                print('''
                =====================
                    Tipo de Venta
                =====================
                ''')
                menu = ['Listar Tipo de Venta', 'Buscar Tipo de Venta', "Nuevo Tipo de Venta", "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_tipo_venta() # Lista las Tipo de Venta de la BD
                elif respuesta == 2:
                    self.buscar_tipo_venta() # Busca Tipo de Venta en base a un ID
                elif respuesta == 3:
                    self.agregar_tipo_venta() # Crea una nuave Tipo de Venta
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def listar_tipo_venta(self):
        print('''
        ==============================
            Lista de Tipo de Venta
        ==============================
        ''')
        tipo_venta = self.tipo_venta.obtener_tipo_venta('id_tipo_venta')
        print(print_table(tipo_venta, ['ID', 'descripción']))
        input("\nPresione una tecla para continuar...")

    def buscar_tipo_venta(self):
        print('''
        ============================
            Buscar Tipo de Venta
        ============================
        ''')
        try:
            id_tipo_venta = input_data("Ingrese el ID de Tipo de Venta >> ", "int")
            tipo_venta = self.tipo_venta.obtener_tipo_venta({'id_tipo_venta': id_tipo_venta})
            print(print_table(tipo_venta, ['ID', 'descripción']))

            if tipo_venta:
                if pregunta("¿Deseas editar Tipo de Venta?"):
                    opciones = ['Editar Tipo de Venta', 'Eliminar Tipo de Venta', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_tipo_venta(id_tipo_venta)
                    elif respuesta == 2:
                        self.eliminar_tipo_venta(id_tipo_venta)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def agregar_tipo_venta(self):
        print('''
        ============================
            Crear Tipo de Venta
        ============================
        ''')
        try:
            descripcion = input_data("Ingrese descripción de Tipo de Venta >> ")
            self.tipo_venta.guardar_tipo_venta({
                'descripcion': descripcion
            })
        except Exception as e:
            print(f'{str(e)}')
        print('''
        =======================================
            Nuevo Tipo de Venta agregado !
        =======================================
        ''')
        self.listar_tipo_venta()

    def editar_tipo_venta(self, id_tipo_venta):
        try:
            descripcion = input_data("Ingrese nueva descripción de Tipo de Venta >> ")
            self.tipo_venta.modificar_tipo_venta({
                'id_tipo_venta': id_tipo_venta
            }, {
                'descripcion': descripcion
            })
        except Exception as e:
            print(f'{str(e)}')
        print('''
        ===============================
            Tipo de Venta Editado !
        ===============================
        ''')

    def eliminar_tipo_venta(self, id_tipo_venta):
        try:
            self.tipo_venta.eliminar_tipo_venta({
                'id_tipo_venta': id_tipo_venta
            })
        except Exception as e:
            print(f'{str(e)}')
        print('''
        ==================================
            Tipo de Venta Eliminado !
        ==================================
        ''')