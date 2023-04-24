class Relatório:
    def __init__(self, título, autor):
        self.cabeçalho = None
        self.título = título
        self.autor = autor
        self.inicializa()
        
    def inicializa(self):
        with open('..dados/cabeçalho.tex') as f:
            self.cabeçalho = f.read()