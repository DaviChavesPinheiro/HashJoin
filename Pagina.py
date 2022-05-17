from Tupla import Tupla
import os

class Pagina:
    def __init__(self):
        self.tuplas = []
        self.qtd_tuplas_ocup = 0

    def add(self, tupla):
        self.tuplas.append(Tupla(tupla))
        self.qtd_tuplas_ocup += 1

    def write(self, path):
        # Escreve todas as tuplas em um .txt
        with open(path, 'w') as f:
            f.writelines("\n".join(list(map(lambda t: ",".join(t.cols), self.tuplas))))
    def write2(self, path):
        # Escreve todas as tuplas em um .txt
        with open(path, 'w') as f:
            f.writelines("\n".join(list(map(lambda tupla: tupla.cols, self.tuplas))))
    def read(self, path):
        # Lê todas as tuplas de um .txt
        with open(path, 'r') as f:
            # Formata cada linha do txt para uma Tupla
            self.tuplas = list(map(lambda line: Tupla(line.strip().split(',')), f.readlines()))
