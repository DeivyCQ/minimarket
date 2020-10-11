from helpers.menu import Menu
from controllers.categoria_controller import Categoria_controller
from controllers.marca_controller import Marca_controller
from controllers.producto_controller import Producto_controller

users = {}

def menu1():
    menu_principal = ['Nuevo Usuario', 'Iniciar Sesion']
    respuesta = Menu(menu_principal).show()
    if respuesta == 1:
        nuevo_usuario()
    elif respuesta == 2:
        iniciar_sesion()

def nuevo_usuario():
    print('''
    ============================
        Registrar Usuario
    ============================
    ''')
    crearusuario = input("Ingresar Nombre de Usuario: ")
    if crearusuario in users:
        print("\nEl Nombre de Usuario existe !\n")
    else:
        createpassword = input("\nIngrese su Contraseña: ")
        users[crearusuario] = createpassword
        print("\nUsuario Creado\n")
        iniciar_sesion()

def iniciar_sesion():
    print('''
    =========================
        Iniciar Seseion
    =========================
    ''')
    usuario = input("Ingrese el Nombre de Usuario: ")
    password = input("Ingrese la Contraseña: ")

    if usuario in users and users[usuario] == password:
        print("\nSesion Iniciada")
        almacenero()
    else:
        print("\nNo Existe el Usuario o Error de Contraseña")

def almacenero():
    try:
        print('''
        ================
            Almacen
        ================
        ''')
        menu_principal = ['Categoría', 'Marca', 'Producto', 'salir' ]
        respuesta = Menu(menu_principal).show()
        if respuesta == 1:
            categoria = Categoria_controller()
            if categoria:
                categoria.menu()
        elif respuesta == 2:
            marca = Marca_controller()
            if marca:
                marca.menu()
        elif respuesta == 3:
            producto = Producto_controller()
            if producto:
                producto.menu()
        elif respuesta == 4:
            pass

        print("\nGracias por utilizar el sistema\n")
    except KeyboardInterrupt:
        print('\n Se interrumpio la aplicación')
    except Exception as e:
        print(f'{str(e)}')

# almacenero()