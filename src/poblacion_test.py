import unittest
from poblacion import *

class TestPoblacion(unittest.TestCase):

    def test_lee_poblaciones(self):
        '''Prueba que los datos se leen correctamente
        '''
        self.assertGreater(len(self.poblaciones), 0)

    def test_calcula_paises(self):
        '''Prueba que la lista de paises es correcta
        '''
        paises = calcula_paises(self.poblaciones)
        self.assertIn('Spain', paises)
        self.assertIn('France', paises)

    def test_filtra_por_paises(self):
        '''Pruebla el filtrado por pais
        '''
        resultado = filtra_por_pais(self.poblaciones, 'Spain')
        self.assertGreater(len(resultado), 0)

    def test_filtra_por_paises_y_anyp(self):
        '''Prueba el filtrado por año y lista de países
        '''
        resultado = filtra_por_paises_y_anyo(self.poblaciones, 2020, {'Spain', 'France'})
        self.asserIsNotNone(filtra_por_pais(self.poblaciones, 'Spain'))

    def test_muestra_comparativa_paises_anyo(self):
        '''Prueba que la funcion genera datos para la comparativa
        '''
        resultado = filtra_por_paises_y_anyo(self.pobolaciones, 2020, {'Spain', 'France'})
        self.assertEqual(len(resultado), 2)

if __name__ == '__main__':
    unittest.main()