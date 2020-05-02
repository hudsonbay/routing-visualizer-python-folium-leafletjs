class Ruta:

    # Initializer / Instance Attributes
    def __init__(self, id, inicio, fin, time_elapsed, hrsExtras, nivelServicio, vehiculo, entregas, listaParadas, km, origin, porTransito, porAtencion, porEspera, porLlenado, porLlenadoUnidades, porLlenadoVolumen, porLlenadoPeso, cantidad, volumen, peso):
        self.id = id
        self.inicio = inicio
        self.fin = fin
        self.time_elapsed = time_elapsed
        self.hrsExtras = hrsExtras
        self.nivelServicio = nivelServicio
        self.vehiculo = vehiculo
        self.entregas = entregas
        self.listaParadas = listaParadas
        self.km = km
        self.origin = origin
        self.porTransito = porTransito
        self.porAtencion = porAtencion
        self.porEspera = porEspera
        self.porLlenado = porLlenado
        self.porLlenadoUnidades = porLlenadoUnidades
        self.porLlenadoVolumen = porLlenadoVolumen
        self.porLlenadoPeso = porLlenadoPeso
        self.cantidad = cantidad
        self.volumen = volumen
        self.peso = peso
