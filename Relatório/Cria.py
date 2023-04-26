import os

class Relatório:
    template_dir = os.path.join('..', 'dados')
    def __init__(self, título, autor, template = 'cabeçalho.tex'):
        self.template = template
        self.cabeçalho = None
        self.título = título
        self.autor = autor
        self.inicializa()
        
    def inicializa(self):
        with open(os.path.join(self.template_dir, 'cabeçalho.tex')) as f:
            self.cabeçalho = f.read()