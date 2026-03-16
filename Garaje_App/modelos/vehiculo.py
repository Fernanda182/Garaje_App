class Vehiculo:
    """
    Clase que representa un vehículo dentro del sistema de garaje.
    """

    def __init__(self, placa, marca, propietario):
        self.placa = placa
        self.marca = marca
        self.propietario = propietario

    def to_list(self):
        """
        Devuelve los datos del vehículo en una lista.
        """
        return [self.placa, self.marca, self.propietario]