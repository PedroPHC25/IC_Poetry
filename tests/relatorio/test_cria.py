import unittest
from Relatório.cria import Relatorio

class TestCria(unittest.TestCase):
    def test_cria_relatorio(self):
        R = Relatorio('Meu relatório', 'Eu mesmo')
        self.assertEqual(R.titulo, 'Meu relatório')
    
    def test_render(self):
        R = Relatorio('Meu relatório', 'Eu mesmo')
        tex = R.render()
        self.assertIn('\\author{ Eu mesmo }', tex)
        self.assertIn('\\title{ Meu relatório }', tex)

    def test_add_section(self):
        R = Relatorio('Meu relatório', 'Eu mesmo')
        R.add_section('\section{primeira seção}')
        tex = R.render()
        self.assertIn('\section{primeira seção}', tex)