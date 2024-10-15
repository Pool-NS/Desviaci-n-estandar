import unittest


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


class TestConjunto(unittest.TestCase):

    def test_vacio(self):
        c = Conjunto([])
        self.assertIsNone(c.media())

    def test_un_elemento(self):
        c = Conjunto([3.5])
        self.assertEqual(c.media(), 3.5)

    def test_varios_elementos(self):
        c = Conjunto([4, 6, 8])
        self.assertEqual(c.media(), 6.0)

    def test_varios_elementos_con_decimal(self):
        c = Conjunto([4, 6, 8, 12.5])
        self.assertAlmostEqual(c.media(), 7.625)

    def test_varios_elementos_con_negativos(self):
        c = Conjunto([3.5, 8, -4.2])
        self.assertAlmostEqual(c.media(), 2.433333333333333)

    def test_todos_ceros(self):
        c = Conjunto([0, 0, 0, 0])
        self.assertEqual(c.media(), 0.0)

    def test_excepcion_datos_no_numericos(self):
        with self.assertRaises(ValueError):
            Conjunto([5, "4.5"])

    def test_excepcion_datos_no_numericos2(self):
        with self.assertRaises(ValueError):
            Conjunto([8, "a"])

    def test_desviacion_estandar(self):
        c = Conjunto([3, 5, 4])
        self.assertAlmostEqual(c.desviacion_estandar(), 1.0)

    def test_desviacion_estandar_excepcion(self):
        c = Conjunto([5])
        with self.assertRaises(ValueError):
            c.desviacion_estandar()


if __name__ == "__main__":
    unittest.main()
