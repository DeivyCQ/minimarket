from helpers.menu import Menu
from helpers.helper import input_data, print_table, pregunta
from users.administrador import menu
from users.almacenero import menu1
from users.cajero import menu2

def iniciar_app():
    try:
        print('''
        =============================================
            Bienvenido al Minimarket Rosita
        =============================================
        ''')
        menu_principal = ['Administración', 'Almacen', 'Caja', 'Salir']
        respuesta = Menu(menu_principal).show()
        if respuesta == 1:
            menu()
        elif respuesta == 2:
            menu1()
        elif respuesta == 3:
            menu2()

        print("\nGracias por utilizar el sistema\n")
    except KeyboardInterrupt:
        print('\n Se interrumpio la aplicación')
    except Exception as e:
        print(f'{str(e)}')

iniciar_app()