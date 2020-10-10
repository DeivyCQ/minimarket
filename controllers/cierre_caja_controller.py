from classes.cierre_caja import Cierre_caja
from helpers.menu import Menu
from helpers.helper import print_table, input_data, pregunta


class cierre_caja_controller():
    def __init__(self):
        self.cierre_caja = Cierre_caja()
       
        self.salir = False

    def menu(self):
        while True:
            try:
                print('''
                =============
                    Caja
                =============
                ''')
                menu = ['Listar caja', 'Buscar cierre de caja', "Nuevo cierre de caja", "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_cierres_de_caja()
                elif respuesta == 2:
                    self.buscar_cierre_de_caja()
                elif respuesta == 3:
                    self.insertar_cierre_de_caja()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')
    
    def listar_cierres_de_caja(self):
        print('''
        ================================
            Lista de Cierres de Caja
        ================================
        ''')
        cierre_caja = self.cierre_caja.obtener_cierre_cajas('cierre_caja_id')
        print(print_table(cierre_caja, ['ID', 'cierre_caja']))
        input("\nPresione una tecla para continuar...")
    def buscar_cierre_de_caja(self):
        print('''
        =============================
            Buscar Cierre de Caja
        =============================
        ''')
        try:
            id_cierre_caja = input_data("Ingrese el ID del cierre de caja >> ", "int")
            cierre_caja = self.alumno.obtener_alumno({'cierre_caja_id': id_cierre_caja})
            print(print_table(cierre_caja, ['ID', 'cierre_caja']))

            if cierre_caja:
                if pregunta("¿Deseas dar mantenimiento al cierre de caja?"):
                    opciones = ['Editar cierre de caja', 'Eliminar cierre de caja', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_cierre_caja(id_cierre_caja)
                    elif respuesta == 2:
                        self.eliminar_cierre_caja(id_cierre_caja)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")
    def insertar_cierre_de_caja(self):
        cierre_caja = input_data("Ingrese el cierre de caja >> ")
        self.cierre_caja.guardar_cierre_caja({
            'cierre_caja': cierre_caja
        })
        print('''
        =================================
            Cierre de Caja agregado !
        =================================
        ''')
        self.listar_cierres_de_caja()

    def editar_cierre_caja(self, id_cierre_caja):
        cierre_caja = input_data("Ingrese el nuevo cierre de caja >> ")
        self.cierre_caja.modificar_cierre_caja({
            'cierre_caja_id': id_cierre_caja
        }, {
            'cierre_caja': cierre_caja
        })
        print('''
        ===================================
            Cierre de Caja Editado !
        ===================================
        ''')
    def eliminar_cierre_caja(self, id_cierre_caja):
        self.cierre_caja.eliminar_cierre_caja({
            'cierre_caja_id': id_cierre_caja
        })
        print('''
        =================================
            Cierre de Caja Eliminado !
        =================================
        ''')