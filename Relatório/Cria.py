from jinja2 import Environment, PackageLoader
import os

class Relatório:
    template_dir = 'dados'
    def __init__(self, título, autor, template = 'cabeçalho.tex'):
        env = Environment(loader = PackageLoader('Poetry'))
        self.template = env.get_template(self.template_file)
        self.cabeçalho = None
        self.título = título
        self.autor = autor
        self.sections = []
        self.context = {'autor': self.autor, 'título': self.título, 'sections': self.sections}
        
    def render(self):
        return self.template.render(self.context)
    
    def add_section(self, section):
        self.sections.append(section)
