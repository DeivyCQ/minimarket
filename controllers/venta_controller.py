from classes.venta import Venta_cabecera, Venta_detalle
from classes.producto import Producto
from classes.tipo_venta import Tipo_venta
from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu

class Venta_controller:
    def __init__(self):
        self.venta_cabecera = Venta_cabecera()
        self.venta_detalle = Venta_detalle()
        self.producto = Producto()
        self.tipo_venta = Tipo_venta()
        self.salir = False

    def menu(self):
        while True:
            try:
                print('''
                =============
                    Venta
                =============
                ''')
                menu = ['Reporte de Ventas', 'Buscar Venta', "Nueva Venta", "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_ventas()
                elif respuesta == 2:
                    self.buscar_venta()
                elif respuesta == 3:
                    self.insertar_venta()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def listar_ventas(self):
        print('''
        ======================
            Lista de Venta
        ======================
        ''')
        ventas_cabecera = self.venta_cabecera.obtener_ventas_cabecera('id_venta')
        ventas_detalle = self.venta_detalle.obtener_ventas_detalle('id_venta')
        print(print_table(ventas_cabecera, ['ID', 'Tipo', 'Comprobante', 'Fecha', 'Precio']))
        input("\nPresione una tecla para continuar...")

    def buscar_venta(self):
        print('''
        ====================
            Buscar Venta
        ====================
        ''')
        try:
            id_venta = input_data("Ingrese el ID de la Venta >> ", "int")   
            venta_cabecera = self.venta_cabecera.obtener_venta_cabecera({'id_venta' : id_venta})
            print(print_table(venta_cabecera, ['ID', 'Tipo', 'Comprobante', 'Fecha', 'Precio']))
            
            if venta_cabecera:
                if pregunta("¿Deseas dar mantenimiento a la Venta?"):
                    opciones = ['Detalle de Venta','Editar Venta', 'Eliminar Venta', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        venta_detalle = self.venta_detalle.obtener_venta_detalle({'id_venta' : id_venta})
                        self.resumen_venta(venta_cabecera, venta_detalle)
                    elif respuesta == 2:
                        self.editar_venta_cabecera(id_venta)
                        self.editar_venta_detalle(id_venta)
                    elif respuesta == 3:
                        self.eliminar_venta_cabecera(id_venta)
                        self.eliminar_venta_detalle(id_venta)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def insertar_venta(self):
        print('''
        ==================================
            Datos de Cabecera de Venta
        ==================================
        ''')
        print('\n>>>>>>>> Elegir Tipo de Venta <<<<<<<<')
        tipo_ventas = self.tipo_venta.obtener_tipos_venta('id_tipo_venta')
        print(print_table(tipo_ventas, ['ID', 'tipo_venta']))
        id_tipo_venta = input_data("Ingrese Tipo de Venta >> ", 'int')
        comprobante = input_data("Ingrese Comprobante de Venta >> ")
        comprobante_busqueda = "'" + comprobante + "'"
        venta_comprobante = self.venta_cabecera.obtener_venta_cabecera({'comprobante' : comprobante_busqueda})
        if venta_comprobante:
            return print(f'Comprobante {comprobante} ya existe en el sistema')
        fecha = input_data("Ingrese Fecha de Venta >> ")
                
        print('''
        ========================
            Detalle de Venta
        ========================
        ''')
        
        venta_detalle_aux = []
        agregar_producto = True
        precio_cabecera_total = 0
        posicion = 0
        descripcion = ''
        cantidad = 0
        unidad_medida = ''
        precio_unitario = 0
        precio_item_total = 0
        while agregar_producto:
            print('\n>>>>>>>> Elegir Producto <<<<<<<<')
            productos = self.producto.obtener_productos('id_producto')
            print(print_table(productos, ['ID', 'Descripción', 'Categoría', 'Marca', 'Stock', 'Precio', 'UM Compra', 'UM Venta'], [3,70,15,15,15,15,20,20]))
            id_producto = input_data("Ingrese ID Producto >> ", "int")
            producto_seleccionado = self.producto.obtener_producto({'id_producto': id_producto})
            # producto_seleccionado = ()
            # for producto in productos:
            #     if id_producto == producto[0]:
            #         producto_seleccionado = producto
            #         break
            posicion += 1
            descripcion = producto_seleccionado[0][1]
            cantidad = input_data("Ingrese Cantidad del Producto >> ", "int")
            unidad_medida = producto_seleccionado[0][7]
            precio_unitario = producto_seleccionado[0][5]
            precio_item_total = cantidad * precio_unitario
            precio_cabecera_total = precio_cabecera_total + precio_item_total
            venta_detalle_aux.append(tuple([999, posicion, id_producto, descripcion, cantidad, unidad_medida, precio_unitario, precio_item_total]))
            if pregunta("¿Deseas adicionar mas productos?"):
                pass
            else:
                agregar_producto = False


        tipo_venta_seleccionado = self.tipo_venta.obtener_tipo_venta({'id_tipo_venta': id_tipo_venta})
        # for id_tipo in tipo_ventas:
        #     if id_tipo_venta == id_tipo[0]:
        #         tipo_venta_seleccionado = id_tipo
        #         break
        tipo_venta_descripcion = tipo_venta_seleccionado[0][1]

        venta_cabecera_aux = []
        venta_cabecera_aux.append(tuple([999, str(id_tipo_venta), comprobante, fecha, precio_cabecera_total]))

        self.resumen_venta(venta_cabecera_aux, venta_detalle_aux)

        if pregunta("Desea confirmar la venta?"):
            id_row = self.venta_cabecera.guardar_venta_cabecera({
                'tipo': id_tipo_venta,
                'comprobante': comprobante,
                'fecha': fecha,
                'precio': precio_cabecera_total
            }, 'id_venta')
            print('id_venta', id_row)
            for pos in venta_detalle_aux:
                self.venta_detalle.guardar_venta_detalle({
                    'id_venta': id_row,
                    'posicion': pos[1],
                    'id_producto': pos[2],
                    'descripcion': pos[3],
                    'cantidad': pos[4],
                    'unidad_medida': pos[5],
                    'precio_unitario': pos[6],
                    'precio_total': pos[7]
                })            
            print('''
            =================================
                Nueva Venta agregado !
            =================================
            ''')
            self.listar_ventas()
        else:
                        print('''
            =======================
                Venta cancelado
            =======================
            ''')

    def editar_venta(self, id_venta):
        print('''
        =================================
            Datos de Detalle de Venta
        =================================
        ''')
        posicion = input_data("Ingrese Posición >> ", "int")
        id_producto = input_data("Ingrese ID Producto >> ", "int")
        descripcion = input_data("Ingrese del Producto >> ")
        cantidad = input_data("Ingrese del Producto >> ", "int")
        unidad_medida = input_data("Ingrese UM del Producto >> ", "int")
        precio_unitario = input_data("Ingrese Precio Unitario >> ", "int")
        precio_item_total = input_data("Ingrese Precio Total >> ", "int")

        self.venta_detalle.modificar_venta_detalle({
            'id_venta_detalle': id_venta
        }, {
            'posicion': posicion,
            'id_producto': id_producto,
            'descripcion': descripcion,
            'cantidad': cantidad,
            'unidad_medida': unidad_medida,
            'precio_unitario': precio_unitario,
            'precio_total': precio_item_total
        })
        print('''
        ==========================
            Venta editado !
        ==========================
        ''')

    def eliminar_venta(self, id_venta):
        self.venta_cabecera.eliminar_venta_cabecera({
            'id_venta_cabecera': id_venta
        })
        self.venta_detalle.eliminar_venta_detalle({
            'id_venta_detalle': id_venta
        })
        print('''
        =========================
            Venta Eliminado !
        =========================
        ''')
    
    def resumen_venta(self, venta_cabecera, venta_detalle):
        tipo_venta = self.tipo_venta.obtener_tipo_venta({'id_tipo_venta': int(venta_cabecera[0][1].strip())})
        venta_detalle_aux = []
        for venta in venta_detalle:
            posicion = venta[1]
            id_producto = venta[2]
            descripcion = venta[3]
            cantidad = venta[4]
            unidad_medida = venta[5]
            precio_unitario = venta[6]
            precio_item_total = venta[7]
            venta_detalle_aux.append(tuple([posicion, id_producto, descripcion, cantidad, unidad_medida, precio_item_total]))
        print(f'''
        ======================================================================
                                DETALLE DE LA VENTA
        ======================================================================
        Tipo de comprobante: {venta_cabecera[0][1].strip()}             Número Comprobante: {venta_cabecera[0][2].strip()}
        Fecha de emisión: {venta_cabecera[0][3]}                Total Venta: {venta_cabecera[0][4]}
        ''')
        print(print_table(venta_detalle_aux, ['Posición', 'ID_Producto', 'Descripción', 'Cantidad', 'UM', 'PU', 'Precio TOTAL'], [2,2,70,10,10,15,15]))