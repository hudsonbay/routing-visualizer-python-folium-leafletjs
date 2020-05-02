from model import Cliente, Destino, Origen, Orden, Producto, Ruta, Parada, Entrega


# recibe por lo general esto como parametro: json_data['input']['listaOrdenes']
def get_orders(json_data):

    lista_ordenes = []

    for orden in json_data:

        # destino
        j = orden['destino']

        # cliente
        i = orden['destino']['cliente']

        # origen
        k = orden['origen']

        # lista de productos
        lista_productos = []

        # parsing clients into objects
        cliente = Cliente.Cliente(i['id'], i['descripcion'], i['rfc'])

        # parsing destinys into objects
        destino = Destino.Destino(j['id'], j['descripcion'], cliente, j['direccion'],
                                  j['latitud'], j['longitud'], j['desde'], j['hasta'], j['flexDesde'], j['flexHasta'])

        # parsing origins into objects
        origen = Origen.Origen(k['id'], k['descripcion'], k['direccion'],
                               k['latitud'], k['longitud'], k['desde'], k['hasta'])

        # parsing productos into objects
        for p in orden['listaProductos']:
            producto = Producto.Producto(p['id'], p['descripcion'], p['cantidad'],
                                         p['volumen'], p['peso'], p['unidadMedida'])
            lista_productos.append(producto)

        # parsing ordenes into objects
        sequence = Orden.Orden(orden['id'], orden['fecha'],
                               orden['duracion'], destino, origen, lista_productos)
        lista_ordenes.append(sequence)

    return lista_ordenes


def get_routes(json_data):
    lista_rutas = []

    for ruta in json_data:

        # stops
        lista_paradas = []

        for parada in ruta['listaParadas']:

            # deliveries for this stop
            lista_entregas = []

            # getting all deliveries from every stop
            for entrega in parada['listaEntregas']:
                delivery = Entrega.Entrega(entrega['id'], entrega['descripcion'], entrega['secuencia'], entrega['direccion'], entrega['idCliente'], entrega['descripcionCliente'], entrega['inicio'], entrega['fin'],
                                           entrega['tEspera'], entrega['km'], entrega['transito'], entrega['latitud'], entrega['longitud'], entrega['robustez'], entrega['cantidad'], entrega['volumen'], entrega['peso'])
                lista_entregas.append(delivery)

            # getting all stops from the json, converting them into objects and appending them to lista_paradas[]
            stop = Parada.Parada(parada['id'], parada['secuencia'], parada['inicio'],
                                 parada['fin'], parada['latitud'], parada['longitud'], lista_entregas)
            lista_paradas.append(stop)

        # parsing origins into objects
        k = ruta['origen']
        origen = Origen.Origen(k['id'], k['descripcion'], k['direccion'],
                               k['latitud'], k['longitud'], k['desde'], k['hasta'])

        route = Ruta.Ruta(ruta['id'], ruta['inicio'], ruta['fin'], ruta['duracion'], ruta['hrsExtras'],
                          ruta['nivelServicio'], ruta['vehiculo'], ruta['entregas'], lista_paradas, ruta['km'], origen, ruta['porTransito'], ruta['porAtencion'], ruta['porEspera'], ruta['porLlenado'], ruta['porLlenadoUnidades'], ruta['porLlenadoVolumen'], ruta['porLlenadoPeso'], ruta['cantidad'], ruta['volumen'], ruta['peso'])
        lista_rutas.append(route)

    return lista_rutas
