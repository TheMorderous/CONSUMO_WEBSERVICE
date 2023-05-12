import requests
import json

#----------------------------------------------LISTAR--------------------------------------------------
def Listar():

    url = 'http://127.0.0.1:5000/listar'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print('Ocurrió un error al procesar la solicitud')
#---------------------------------------------BUSCAR--------------------------------------------------
def Buscar():
    nombre = input("Ingresa el nombre que deseas buscar: ")
    url = f'http://127.0.0.1:5000/buscar/{nombre}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print('Error al realizar la solicitud')

#----------------------------------------------ACTUALIZAR--------------------------------------------------
def Actualizar():
    print('Seleccionaste la opcion Comprar Libros')
    # Datos del pedido
    # Pedir al usuario que ingrese el id y la cantidad de cada libro
    libros = []
    while True:
        id_libro = input("Ingrese el id del libro o 'q' para salir: ")
        if id_libro == 'q':
            break
        cantidad = input("Ingrese la cantidad del libro: ")
        libros.append({"id_libro": int(id_libro), "cantidad": int(cantidad)})

    # Pedir al usuario que ingrese el id de la sucursal
    id_sucursal = input("Ingrese el id de la sucursal: ")

    # Definir el JSON con los datos del pedido
    pedido = {
        "libros": libros,
        "id_sucursal": int(id_sucursal)
    }

    # Hacer la solicitud PUT al endpoint /actualizar_libros
    url = "http://127.0.0.1:5000/actualizar_libros"
    headers = {"Content-Type": "application/json"}
    response = requests.put(url, headers=headers, data=json.dumps(pedido))

    # Obtener la respuesta del servidor
    print(response.text)
#----------------------------------------------PEDIDO--------------------------------------------------
def Pedido():
    print("Seleccionaste la opción Factura")

    # Generar pedido
    url_pedido = "http://127.0.0.1:5000/factura"
    # Datos del pedido
    # Pedir al usuario que ingrese el id y la cantidad de cada libro
    libros = []
    while True:
        id_libro = input("Ingrese el id del libro o 'q' para salir: ")
        if id_libro == 'q':
            break
        cantidad = input("Ingrese la cantidad del libro: ")
        libros.append({"id_libro": int(id_libro), "cantidad": int(cantidad)})
    # Pedir al usuario que ingrese el id de la sucursal
    id_sucursal = input("Ingrese el id de la sucursal: ")
    # Definir el JSON con los datos del pedido
    payload = {
        "libros": libros,
        "id_sucursal": int(id_sucursal)
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response_pedido = requests.post(url_pedido, headers=headers, data=json.dumps(payload))
    print(response_pedido.text)
    # Mostrar id del último pedido
    url_ultimo_pedido = 'http://localhost:5000/ultimo_pedido'
    response_id_pedido = requests.get(url_ultimo_pedido)
    if response_id_pedido.status_code == 200:
        id_pedido = response_id_pedido.text
        print("El último pedido es:", id_pedido)
    else:
        print("Error en la solicitud:", response_id_pedido.status_code)

#----------------------------------------------MENU--------------------------------------------------
# Menú principal
while True:
    print("==== BIENVENIDO A UNA SUPER LIBRERIA ====")
    print("=========== ¿QUE DESEA HACER? ===========")
    print("1. Listar Libros")
    print("2. Buscar Libros")
    print("3. Comprar Libros")
    print("4. Factura Compra")
    print('5. Salir')

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        Listar()
    elif opcion == 2:
        Buscar()
    elif opcion == 3:
        Actualizar()
    elif opcion == 4:
        Pedido()
    elif opcion == 5:
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción del menú.")