from model import Client, Destiny, Origin, Order, Product, Ruta, Parada, Entrega


# recibe por lo general esto como parametro: json_data['input']['listaOrderes']
def get_orders(json_data):

    lista_orderes = []

    for order in json_data:

        # destiny
        j = order['destiny']

        # client
        i = order['destiny']['client']

        # origin
        k = order['origin']

        # lista de products
        lista_products = []

        # parsing clients into objects
        client = Client.Client(i['id'], i['descripcion'], i['rfc'])

        # parsing destinys into objects
        destiny = Destiny.Destiny(j['id'], j['descripcion'], client, j['direccion'],
                                  j['latitud'], j['longitud'], j['desde'], j['hasta'], j['flexDesde'], j['flexHasta'])

        # parsing origins into objects
        origin = Origin.Origin(k['id'], k['descripcion'], k['direccion'],
                               k['latitud'], k['longitud'], k['desde'], k['hasta'])

        # parsing products into objects
        for p in order['listaProducts']:
            product = Product.Product(p['id'], p['descripcion'], p['cantidad'],
                                      p['volumen'], p['peso'], p['unidadMedida'])
            lista_products.append(product)

        # parsing orderes into objects
        sequence = Order.Order(order['id'], order['fecha'],
                               order['duracion'], destiny, origin, lista_products)
        lista_orderes.append(sequence)

    return lista_orderes


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
                delivery = Entrega.Entrega(entrega['id'], entrega['descripcion'], entrega['secuencia'], entrega['direccion'], entrega['idClient'], entrega['descripcionClient'], entrega['inicio'], entrega['fin'],
                                           entrega['tEspera'], entrega['km'], entrega['transito'], entrega['latitud'], entrega['longitud'], entrega['robustez'], entrega['cantidad'], entrega['volumen'], entrega['peso'])
                lista_entregas.append(delivery)

            # getting all stops from the json, converting them into objects and appending them to lista_paradas[]
            stop = Parada.Parada(parada['id'], parada['secuencia'], parada['inicio'],
                                 parada['fin'], parada['latitud'], parada['longitud'], lista_entregas)
            lista_paradas.append(stop)

        # parsing origins into objects
        k = ruta['origin']
        origin = Origin.Origin(k['id'], k['descripcion'], k['direccion'],
                               k['latitud'], k['longitud'], k['desde'], k['hasta'])

        route = Ruta.Ruta(ruta['id'], ruta['inicio'], ruta['fin'], ruta['duracion'], ruta['hrsExtras'],
                          ruta['nivelServicio'], ruta['vehiculo'], ruta['entregas'], lista_paradas, ruta['km'], origin, ruta['porTransito'], ruta['porAtencion'], ruta['porEspera'], ruta['porLlenado'], ruta['porLlenadoUnidades'], ruta['porLlenadoVolumen'], ruta['porLlenadoPeso'], ruta['cantidad'], ruta['volumen'], ruta['peso'])
        lista_rutas.append(route)

    return lista_rutas
