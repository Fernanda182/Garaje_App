class GarajeServicio:
    """
    Clase encargada de gestionar los vehículos registrados.
    """

    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        """
        Agrega un vehículo a la lista del garaje.
        """
        self.vehiculos.append(vehiculo)

    def listar_vehiculos(self):
        """
        Devuelve la lista de vehículos registrados.
        """
        return self.vehiculos