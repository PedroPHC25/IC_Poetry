import unittest
from Relatório.Cria import Relatorio

class TestCria(unittest.TestCase):
    def test_cria_relatorio(self):
        R = Relatorio('Meu relatório', 'Eu mesmo')
        self.assertEqual(R.titulo, 'Meu relatório')