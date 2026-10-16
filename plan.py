class Plan:
    def __init__(self, nombre, precio, con_anuncios):
        self.nombre = nombre
        self.precio = precio
        self.con_anuncios = con_anuncios

    def get_nombre(self):
        return self.nombre

    def get_precio(self):
        return self.precio

    def tiene_anuncios(self):
        return self.con_anuncios

    def calcular_precio_total(self, meses):
        #se le da un 10% de descuento desde 12 meses
        total= self.precio * meses
        if meses >= 12:
            total *= 0.9  # Aplicar descuento del 10%
        return total

    def mostrar_info(self):
        if self.con_anuncios:
            anuncios = "con anuncios"
        else:
            anuncios = "sin anuncios"   
        return f"Plan: {self.nombre}, Precio: ${self.precio}, {anuncios}"
    
    