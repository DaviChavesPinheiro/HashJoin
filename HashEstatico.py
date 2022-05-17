import uuid
import os
from Page import Page
import json

class HashEstatico:
    def __init__(self, buckets):
        self.buckets = buckets
        # Pasta contendo todos os buckets desse indice. (Apenas para organizacão).
        self.dir = "./" + str(uuid.uuid4())
        
        # Cria a pasta que vai guardar todos os buckets desse indice
        os.mkdir(self.dir)
    
    # Funcão de HASH que retorna um inteiro entre 0 e (buckets - 1)
    def HASH(self, x):
        return hash(x) % (self.buckets)

    def add(self, column, p_registro):
        hs = self.HASH(column)
        
        # Procura uma página no bucket que esteja disponivel. Caso estejam todas cheias, cria uma nova
        i = 0
        while (True):
            # Caso a página i não exista, cria uma e adicione a entrada a ela
            if(not os.path.exists(os.path.join(self.dir, "{}-{}.txt".format(hs, i)))):
                Page.data = ["{},{}\n".format(column, p_registro)]
                Page.write(os.path.join(self.dir, "{}-{}.txt".format(hs, i)))
                break
            else:
                # Lê a página cadidata
                Page.read(os.path.join(self.dir, "{}-{}.txt".format(hs, i)))
                
                # Se a página não está cheia
                if(len(Page.data) < 12):
                    # Adiciona uma entrada
                    Page.data.append("{},{}\n".format(column, p_registro))
                    Page.write(os.path.join(self.dir, "{}-{}.txt".format(hs, i)))
                    break
            i += 1
    
    def find(self, column):
        hs = self.HASH(column)
        
        # Tuplas que atendem ao predicado de igualde
        tuplas = []

        # Checa todas as páginas
        i = 0
        while (True):
            # Caso a página exista
            if(os.path.exists(os.path.join(self.dir, "{}-{}.txt".format(hs, i)))):
                # Leia a página e filtre só as entradas que atendem ao predicado
                Page.read(os.path.join(self.dir, "{}-{}.txt".format(hs, i)))
                tuplas.extend(list(map(lambda entry: entry.strip().split(',', 1)[1], filter(lambda line: line.split(',')[0] == str(column), Page.data))))
            else:
                # Já checamos todas as páginas
                break
            i += 1
        return tuplas 
