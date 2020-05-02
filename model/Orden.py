class Orden:

    # Initializer / Instance Attributes
    def __init__(self, id, fecha, duracion, destino, origen, listaProductos):
        self.id = id
        self.fecha = fecha
        self.duracion = duracion
        self.destino = destino
        self.origen = origen
        self.listaProductos = listaProductos
