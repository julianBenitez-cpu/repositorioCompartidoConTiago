from kilometraje import vehiculo

autito = vehiculo('rojo', 'Fiat', 'Chronos', 'ab 294 mn', 0)

info = autito.mostrarDatos()
print(info)

while True:
    kilometros_avanzados = int(input('¿Cuantos kilometros queres recorrer? Si desea salir ingrese "0".'))
    
    if kilometros_avanzados == 0:
        break

    elif kilometros_avanzados > 0:
        autito.conducir(kilometros_avanzados)
        print(f'El nuevo kilometraje del vehiculo es: ', autito.get_kilometraje())

    else:
        print('No se puede avanzar menos que 0')
    