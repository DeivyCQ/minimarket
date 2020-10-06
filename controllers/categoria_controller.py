from classes.categoria import Categoria
from helpers.menu import Menu
from helpers.helper import print_table, input_data, pregunta

class Categoria_controller:
    def __init__(self):
        self.categoria = Categoria()
        self.salir = False
    def menu(self):
        while True:
            try:
                print('''
                =============================
                    Categoría de Producto
                =============================
                ''')
                menu = ['Listar Categoría', 'Buscar Categoría', "Nueva Categoría", "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_categoria() # Lista las Categorías de la BD
                elif respuesta == 2:
                    self.buscar_categoria() # Busca Categoría en base a un ID
                elif respuesta == 3:
                    self.agregar_categoria() # Crea una nuave Categoría
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def listar_categoria(self):
        print('''
        ======================================
            Lista de Categoría de Producto
        ======================================
        ''')
        categoria = self.categoria.obtener_categoria('id_categoria')
        print(print_table(categoria, ['ID', 'descripción']))
        input("\nPresione una tecla para continuar...")

    def buscar_categoria(self):
        print('''
        ====================================
            Buscar Categoría de Producto
        ====================================
        ''')
        try:
            id_categoria = input_data("Ingrese el ID del categoría >> ", "int")
            categoria = self.categoria.obtener_categoria({'id_categoria': id_categoria})
            print(print_table(categoria, ['ID', 'descripción']))

            if categoria:
                if pregunta("¿Deseas editar Categoría de producto?"):
                    opciones = ['Editar categoría', 'Eliminar Categoría', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_categoria(id_categoria)
                    elif respuesta == 2:
                        self.eliminar_categoria(id_categoria)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def agregar_categoria(self):
        print('''
        ===================================
            Crear Categoría de Producto
        ===================================
        ''')
        try:
            descripcion = input_data("Ingrese descripción de la Categoría >> ")
            self.categoria.guardar_categoria({
                'descripcion': descripcion
            })
        except Exception as e:
            print(f'{str(e)}')
        print('''
        ==============================================
            Nueva Categoría de Producto agregado !
        ==============================================
        ''')
        self.listar_categoria()

    def editar_categoria(self, id_categoria):
        try:
            descripcion = input_data("Ingrese el nuevo nombre del Categoría de producto >> ")
            self.categoria.modificar_categoria({
                'id_categoria': id_categoria
            }, {
                'descripcion': descripcion
            })
        except Exception as e:
            print(f'{str(e)}')
        print('''
        =======================================
            Categoría de Producto Editado !
        =======================================
        ''')

    def eliminar_categoria(self, id_categoria):
        try:
            self.categoria.eliminar_categoria({
                'id_categoria': id_categoria
            })
        except Exception as e:
            print(f'{str(e)}')
        print('''
        ====================================
            Categoría de Producto Eliminado !
        ====================================
        ''')