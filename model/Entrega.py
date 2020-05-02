class Entrega:

    # Initializer | Instance Attributes
    def __init__(self, id, descripcion, secuencia, direccion, idClient, descripcionClient, inicio, fin, tEspera, km, transito, latitud, longitud, robustez, cantidad, volumen, peso):
        self.id = id
        self.descripcion = descripcion
        self.secuencia = secuencia
        self.direccion = direccion
        self.idClient = idClient
        self.descripcionClient = descripcionClient
        self.inicio = inicio
        self.fin = fin
        self.tEspera = tEspera
        self.km = km
        self.transito = transito
        self.latitud = latitud
        self.longitud = longitud
        self.robustez = robustez
        self.cantidad = cantidad
        self.volumen = volumen
        self.peso = peso
