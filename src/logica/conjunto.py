class Conjunto:
    def __init__(self, conjunto):
        if not all(isinstance(x, (int, float)) for x in conjunto):
            raise ValueError("Todos los elementos deben ser números.")
        self.__conjunto = conjunto

    def media(self):
        if len(self.__conjunto) == 0:
            return None
        return sum(self.__conjunto) / len(self.__conjunto)

    def desviacion_estandar(self):
        if len(self.__conjunto) < 2:
            raise ValueError("Se requieren al menos dos elementos para calcular la desviación estándar.")

        mean = self.media()
        variance = sum((x - mean) ** 2 for x in self.__conjunto) / (len(self.__conjunto) - 1)
        return variance ** 0.5
