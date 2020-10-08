from classes.rol import Rol
from helpers.menu import Menu
from helpers.helper import print_table, input_data, pregunta

class Rol_controller:
    def __init__(self):
        self.rol = Rol()
        self.salir = False
    def menu(self):
        while True:
            try:
                print('''
                =============================
                    Rol de Usuario
                =============================
                ''')
                menu = ['Listar Rol', 'Buscar Rol', "Nuevo Rol", "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_rol() # Lista las Marcas de la BD
                elif respuesta == 2:
                    self.buscar_rol() # Busca Rol en base a un ID
                elif respuesta == 3:
                    self.agregar_rol() # Crea una nuave Rol
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def listar_rol(self):
        print('''
        ======================================
            Lista de Rol de Usuario
        ======================================
        ''')
        rol = self.rol.obtener_rol('id_rol')
        print(print_table(rol, ['ID', 'descripción']))
        input("\nPresione una tecla para continuar...")

    def buscar_rol(self):
        print('''
        ====================================
            Buscar Rol de Usuario
        ====================================
        ''')
        try:
            id_rol = input_data("Ingrese el ID de Rol >> ", "int")
            rol = self.rol.obtener_rol({'id_rol': id_rol})
            print(print_table(rol, ['ID', 'descripción']))

            if rol:
                if pregunta("¿Deseas editar Rol de Usuario?"):
                    opciones = ['Editar Rol', 'Eliminar Rol', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_rol(id_rol)
                    elif respuesta == 2:
                        self.eliminar_rol(id_rol)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def agregar_rol(self):
        print('''
        ===============================
            Crear Rol de Usuario
        ===============================
        ''')
        try:
            descripcion = input_data("Ingrese descripción de Rol >> ")
            self.rol.guardar_rol({
                'descripcion': descripcion
            })
        except Exception as e:
            print(f'{str(e)}')
        print('''
        ==============================================
            Nuevo Rol de Usuario agregado !
        ==============================================
        ''')
        self.listar_rol()

    def editar_rol(self, id_rol):
        try:
            descripcion = input_data("Ingrese nueva descripción de Rol de Usuario >> ")
            self.rol.modificar_rol({
                'id_rol': id_rol
            }, {
                'descripcion': descripcion
            })
        except Exception as e:
            print(f'{str(e)}')
        print('''
        =======================================
            Rol de Usuario Editado !
        =======================================
        ''')

    def eliminar_rol(self, id_rol):
        try:
            self.rol.eliminar_rol({
                'id_rol': id_rol
            })
        except Exception as e:
            print(f'{str(e)}')
        print('''
        ====================================
            Rol de Usuario Eliminado !
        ====================================
        ''')