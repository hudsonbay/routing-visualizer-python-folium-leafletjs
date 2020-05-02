class Entrega:

    # Initializer | Instance Attributes
    def __init__(self, id, description, secuencia, direccion, idClient, clientDescription, inicio, fin, tEspera, km, transito, latitude, longitude, robustez, cantidad, volumen, peso):
        self.id = id
        self.description = description
        self.secuencia = secuencia
        self.direccion = direccion
        self.idClient = idClient
        self.clientDescription = clientDescription
        self.inicio = inicio
        self.fin = fin
        self.tEspera = tEspera
        self.km = km
        self.transito = transito
        self.latitude = latitude
        self.longitude = longitude
        self.robustez = robustez
        self.cantidad = cantidad
        self.volumen = volumen
        self.peso = peso
