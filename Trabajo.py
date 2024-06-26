import os
import pyfiglet
from datetime import date
from datetime import datetime, timedelta

fecha_inicio = datetime(1111,11,11)
fecha_final   = datetime(9999,12,31)

os.system("cls")

today=date.today()
format = today.strftime("%d-%m-%Y")
productos = "productos.txt"
ventas = "ventas_prod.txt"
folio = 10000
elemento = 0
id=0
''' Venta de relojes con dos categorías (Normales y Lujosos) '''

productos = []
ventas = []

def leer_datos_productos(archivo):
    # Lista para almacenar los datos
    lista_datos = []

    # Abrimos el archivo en modo lectura
    with open(archivo, 'r') as file:
        # Leemos cada línea del archivo
        for linea in file:
            linea = linea.strip()
            datos = linea.split(',')

            # Validación del número de elementos
            if len(datos) < 6:
                print(f"Línea con formato incorrecto: {linea}")
                continue

            try:
                id_producto = datos[0]
                nombre = datos[1]
                marca = datos[2]
                modelo = datos[3]
                precio = int(datos[4])
                stock = int(datos[5])

                # Añadir a la lista de datos
                lista_datos.append([id_producto, nombre, marca, modelo, precio, stock])

            except ValueError as e:
                print(f"Error de valor en la línea: {linea} -> {e}")

    return lista_datos

# Llamamos a la función y almacenamos el resultado en una variable
productos = leer_datos_productos("productos.txt")


leer_datos_productos("productos.txt")


def mostrar_tabla_relojes():
    tabla_relojes = [["ID", "Serial", "Marca","modelo", "Precio", "Stock"]] 
    for producto in productos:          
        id_producto = producto[0]       
        serial = producto[1]   
        marca = producto[2]   
        modelo = producto[3]   
        stock = producto[4]  
        precio = producto[5]
        fila = [id_producto, serial, marca, modelo, stock,precio] 
        tabla_relojes.append(fila) 
    col_widths = [max(len(str(value)) for value in column) for column in zip(*tabla_relojes)]
    separador = "-+-".join('-' * width for width in col_widths)
    for i, row in enumerate(tabla_relojes):
        print(" | ".join(f"{str(value).ljust(width)}" for value, width in zip(row, col_widths)))
        if i == 0:
            print(separador)

def leer_datos_ventas(ventas):
    # Lista para almacenar los datos
    lista_ventas = []

    # Abrimos el archivo en modo lectura
    with open(ventas, 'r') as file:
        # Leemos cada línea del archivo
        for linea in file:
            linea = linea.strip()
            datos = linea.split(',')

            # Validación del número de elementos
            if len(datos) < 5:
                print(f"Línea con formato incorrecto: {linea}")
                continue

            try:
                folio = int(datos[0])
                fecha = datos[1]
                id = datos[2]
                stock = int(datos[3])
                precio = int(datos[4])

                # Añadir a la lista de datos
                lista_ventas.append([folio, fecha, id, stock, precio])

            except ValueError as e:
                print(f"Error de valor en la línea: {linea} -> {e}")

    return lista_ventas

# Llamamos a la función y almacenamos el resultado en una variable
ventas = leer_datos_ventas("ventas_prod.txt")


leer_datos_ventas("ventas_prod.txt")

def mostrar_tabla_ventas():
    tabla_ventas = [["Folio", "Fecha", "ID","Cantidad", "Precio"]] 
    for venta in ventas:          
        folio = venta[0]       
        fecha = venta[1]   
        id = venta[2]   
        cantidad = venta[3]  
        precio = venta[4]
        fila = [folio, fecha, id, cantidad, precio] 
        tabla_ventas.append(fila) 
    col_widths = [max(len(str(value)) for value in column) for column in zip(*tabla_ventas)]
    separador = "-+-".join('-' * width for width in col_widths)
    for i, row in enumerate(tabla_ventas):
        print(" | ".join(f"{str(value).ljust(width)}" for value, width in zip(row, col_widths)))
        if i == 0:
            print(separador)

def get_folio(folio):
    if leer_datos_ventas != 0:
        for venta in ventas:
            folio = venta[0]
    return folio



def ultimo_id():
    for producto in productos:
        id = int(producto[0])
        id = id+1
    return id



def agregar_venta(folio, fecha, id, cantidad, precio):
    # Abrimos el archivo en modo de agregar ('a')
    ventas='ventas_prod.txt'
    # a append
    with open(ventas, 'a') as file:
        # Escribimos el nuevo registro en una nueva línea
        
        file.write(f"\n{folio},{fecha},{str(id)},{cantidad},{precio}")

def agregar_producto(id,modelo,marca,nombre,precio,stock):
    # Abrimos el archivo en modo de agregar ('a')
    productos="productos.txt"
    # a append
    with open(productos, 'a') as file:
        # Escribimos el nuevo registro en una nueva línea
        
        file.write(f"\n{id},{modelo},{marca},{nombre},{precio},{stock}")


def buscar_id(id):
    for producto in productos:
        id_producto = producto[0]
        if id_producto == id:
            print("Producto encontrado")
            print("\nID-ID:",producto[0])
            print("SERIAL:",producto[1])
            print("MARCA:",producto[2])
            print("MODELO:",producto[3])
            print("VALOR:",producto[4])
            print("STOCK:",producto[5])

def eliminar(id):
    for producto in productos:
        id_producto = producto[0]
        if id_producto == id:
            productos.remove(producto)
            print("Producto eliminado")
            os.system("pause")


op=0
op2=0
op3=0


print(pyfiglet.figlet_format("Relojeria"))
os.system("pause")
while True:
    os.system("cls")
    print("Último folio: ",get_folio(folio))
    print("Fecha actual: ",format)
    print("""
                VENTA DE RELOJES
          ----------------------------
          1. Vender productos
          2. Reportes
          3. Mantenedor de productos
          4. Administración
          5. Salir
          ----------------------------""")
    try:
        op=int(input("Seleccione una opción: "))
        match op:
            case 1:
                    os.system("cls")
                    mostrar_tabla_relojes()
                    id=input("Ingrese el código del producto: ")
                    for producto in productos:
                        id_producto = producto[0]
                        if id_producto == id:
                            print("Producto encontrado")
                            print("\nID-ID:",producto[0])
                            print("SERIAL:",producto[1])
                            print("MARCA:",producto[2])
                            print("MODELO:",producto[3])
                            print("VALOR:",producto[4])
                            print("STOCK:",producto[5])
                            stock = producto[5]
                    cantidad_items = int(input("¿Cuantos desea comprar?: "))

                    if cantidad_items >= 0 and cantidad_items <= stock:
                        folio = get_folio(folio)+1
                        fecha = format
                        id = producto[0]
                        cantidad = cantidad_items
                        precio = producto[4] * cantidad_items
                        producto[5]=producto[5]-cantidad_items
                        agregar_venta(folio, fecha, id, cantidad, precio)
                        print("Venta realizada con exito!")
                        os.system("pause")
                        
                    else:
                        print("Error, la cantidad supera el stock")
                        os.system("pause")

            case 2:
                os.system("cls")
                op=0
                while op<=4:
                    os.system("cls")
                    print('''
                            REPORTE DE VENTAS
                    -----------------------------------          
                    1. General de ventas (con total)
                    2. Ventas por fecha específica (con total)
                    3. Ventas por rango de fecha (con total)
                    4. Salir al menú principal
                    -----------------------------------
                    
                    ''')
                    op=int(input("ingrese una opción 1-4: "))
                    
                    match op:
                        case 1:
                            os.system("cls")
                            mostrar_tabla_ventas()
                            os.system("pause")
                        case 2:
                            os.system("cls")
                            print("\n Ventas por fecha específica\n")
                            fecha=input("Ingrese fecha(aa-mm-aaaa): ")
                            a=0
                            for venta in ventas:
                                if venta[1] == fecha:
                                    print("Venta encontrada")
                                    a=a+venta[4]
                                    print(venta[0]," ",venta[1]," ",venta[2])
                                    print("Total: ", a)
                            
                            else:
                                print("no hay más ventas que mostrar.")
                            
                            os.system("pause")
                        case 3:
                            os.system("cls")
                            print("\n ventas por fecha de rango\n")  
                            fecha_inicio=input("ingrese fecha inicial(aa-mm-aaaa): ")        
                            fecha_final=input("Ingrese fecha final(aa-mm-aaaa): ")
                            a=0
                            for venta in ventas:
                                if venta[1] >= fecha_inicio and venta[1] <= fecha_final:
                                    a=a+venta[4]
                                    print(venta[0]," ",venta[1]," ",venta[2])
                           
                           
                            else:
                                print("No hay más fechas.")

                            print("Su Total es:", a)
                            os.system("pause")
                            break
                        case 4:
                            break

            case 3:
                os.system("cls")
                print("MANTENEDOR DE PRODUCTOS")
                print("1 Agregar")
                print("2 Buscar por ID")
                print("3 Elimina por ID")
                print("4 ** Modificar **")
                print("5 Listar")
                print("6 volver al menu pricipal\n")
                op2=int(input("Ingrese una opción [1-6]: "))

                match op2:
                        
                    case 1:
                        id = ultimo_id()
                        try:
                            os.system("cls")
                            print("\n AGREGAR PRODUCTOS \n")
                            print("Agregar datos a lista reloj")
                            modelo=input("ingrese por modelo: ")
                            marca=input("ingrese marca: ") 
                            nombre=input("ingrese nombre: ")
                            precio=int(input("ingrese precio a modificar: "))
                            stock=int(input("stock de productos: "))
                            agregar_producto(id,modelo,marca,nombre,precio,stock)
                            productos.append([id,modelo,marca,nombre,precio,stock])
                            os.system("pause")
                        except:
                            print("Error")

                    case 2:
                        os.system("cls")
                        id=input("Ingrese el código del producto: ")
                        for producto in productos:
                            id_producto = producto[0]
                            if id_producto == id:
                                print("Producto encontrado")
                                print("\nID-ID:",producto[0])
                                print("SERIAL:",producto[1])
                                print("MARCA:",producto[2])
                                print("MODELO:",producto[3])
                                print("VALOR:",producto[4])
                                print("STOCK:",producto[5])
                                os.system("pause")
                                break
                        else:
                            print("Producto no encontrado")
                            os.system("pause")
                            break
                    case 3:
                        os.system("cls")
                        id = input("ingrese una id a eliminar: ")
                        for producto in productos:
                            id_producto = producto[0]
                            if id_producto == id:
                                eliminar(id)
                                mostrar_tabla_relojes()
                                os.system("pause")
                                break
                        else:
                            print("Producto no encontrado")
                            os.system("pause")

                    case 4:
                        id_producto = input("ingrese el id a buscar: ")
                        for producto in productos:
                            id_encontrada = producto[0]
                            if id_encontrada == id_producto:
                                cantidad_items =int(input("Cuantos productos desea agregar? "))
                                producto[5]+=cantidad_items
                    case 5:
                        mostrar_tabla_relojes()
                        os.system('pause')

            case 4:
                os.system("cls")
                op=0
                while op <=3:
                    print('''
                            ADMINISTRACION
                    -----------------------------------          
                    1. CARGAR DATOS
                    2. RESPALDAR DATOS (GRABAR ACTUALIZAR)
                    3. SALIR
                    -----------------------------------
                    
                    ''')
                    op=int(input("ingrese una opción 1-3: "))
                    match op:
                        case 1:
                            productos=leer_datos_productos("productos.txt")
                            ventas=leer_datos_ventas("ventas_prod.txt")
                            get_folio(folio)
                        case 2:
                            leer_datos_productos(productos) 
                            leer_datos_ventas(ventas)
                            get_folio(folio)
    except:
        print('Rango no valido')
