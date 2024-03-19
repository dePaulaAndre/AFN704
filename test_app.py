import unittest
from app import soma, subtracao, multiplicacao, divisao



class TestSoma(unittest.TestCase):

    def test_positivos(self):
        self.assertEqual(soma(2, 3), 5)

    def test_negativos(self):
        self.assertEqual(soma(-2, -3), -5)

    def test_decimais(self):
        self.assertAlmostEqual(soma(2.5, 3.5), 6.0)

    def test_zero(self):
        self.assertEqual(soma(0, 0), 0)

    def test_negativo_positivo(self):
        self.assertEqual(soma(-4, 8), 4)


class TestSubtracao(unittest.TestCase):
        
    def test_negativo_positivo(self):
        self.assertEqual(subtracao(-8, 2), -10)

    def test_positivos(self):
        self.assertEqual(subtracao(3, 2), 1)

    def test_negativos(self):
        self.assertEqual(subtracao(-2, -3), 1)

    def test_decimais(self):
        self.assertAlmostEqual(subtracao(3.5, 2.5), 1.0)

    def test_zero(self):
        self.assertEqual(subtracao(0, 0), 0)


class TestMultiplicacao(unittest.TestCase):
        
    def test_negativo_positivo(self):
        self.assertEqual(multiplicacao(-8, 2), -16)

    def test_positivos(self):
        self.assertEqual(multiplicacao(3, 2), 6)

    def test_negativos(self):
        self.assertEqual(multiplicacao(-2, -3), 6)

    def test_decimais(self):
        self.assertAlmostEqual(multiplicacao(3.5, 2), 7)

    def test_zero(self):
        self.assertEqual(multiplicacao(0, 0), 0)


class TestDivisao(unittest.TestCase):
        
    def test_positivos(self):
        self.assertEqual(divisao(6, 3), 2)

    def test_positivo_negativo(self):
        self.assertEqual(divisao(6, -3), -2)

    def test_negativo_positivo(self):
        self.assertEqual(divisao(-6, 3), -2)

    def test_zero(self):
        self.assertIsNone(divisao(5, 0))

def quadrado(numero):
    resultado = numero ** 2
    return resultado

class TestQuadrado(unittest.TestCase):
    
    def test_quadrado(self):
        self.assertEqual(quadrado(5), 25)

    def test_quadrado_zero(self):
        self.assertEqual(quadrado(0), 0)

    def test_quadrado_um(self):
        self.assertEqual(quadrado(1), 1)

def triplo_numeros(numeros):
    return list(map(lambda x: x * 3, numeros))

class TestTriploNumeros(unittest.TestCase):
    
    def test_triplo_numeros(self):
        numeros = [1, 2, 3, 4, 5]
        resultado_esperado = [3, 6, 9, 12, 15]
        self.assertEqual(triplo_numeros(numeros), resultado_esperado)

    def test_triplo_numeros_zerados(self):
        numeros = [0,0,0,0,0]
        resultado_esperado = [0,0,0,0,0]
        self.assertEqual(triplo_numeros(numeros), resultado_esperado)

    def test_triplo_numeros_negativos(self):
        numeros = [-1, -2, -3, -4, -5]
        resultado_esperado = [-3, -6, -9, -12, -15]
        self.assertEqual(triplo_numeros(numeros), resultado_esperado)


def Calculador(operador):
    def calcular(x, y):
        if operador == '+':
            return x + y
        elif operador == '-':
            return x - y
        elif operador == '*':
            return x * y
        elif operador == '/':
            if y != 0:
                return x / y
            else:
                return "Erro: Divisão por zero!"
        else:
            return "Erro: Operador inválido!"
    
    return calcular

class TestCalculador(unittest.TestCase):
    
    def test_soma(self):
        calculando_soma = Calculador('+')
        self.assertEqual(calculando_soma(5, 3), 8)
    
    def test_subtracao(self):
        calculando_subtracao = Calculador('-')
        self.assertEqual(calculando_subtracao(10, 3), 7)
    
    def test_multiplicacao(self):
        calculando_multiplicacao = Calculador('*')
        self.assertEqual(calculando_multiplicacao(4, 5), 20)
    
    def test_divisao(self):
        calculando_divisao = Calculador('/')
        self.assertEqual(calculando_divisao(10, 2), 5)
        self.assertEqual(calculando_divisao(10, 0), "Erro: Divisão por zero!")
    
    def test_operador_invalido(self):
        calculando_invalido = Calculador('%')
        self.assertEqual(calculando_invalido(10, 5), "Erro: Operador inválido!") 

    def criar_listas_pares_impares(numMax):
        Par = [x for x in range(1, numMax + 1) if x % 2 == 0]
        Impar = [x for x in range(1, numMax + 1) if x % 2 != 0]
        return Par, Impar

    class TestCriarListas(unittest.TestCase):
        
        def test_criar_listas_pares_impares(self):
            numMax = 10
            pares_esperados = [2, 4, 6, 8, 10]
            impares_esperados = [1, 3, 5, 7, 9]
            pares, impares = criar_listas_pares_impares(numMax)
            self.assertEqual(pares, pares_esperados)
            self.assertEqual(impares, impares_esperados) 
            
if __name__ == '__main__':
    unittest.main()
