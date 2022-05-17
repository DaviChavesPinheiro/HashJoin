import csv
import os
from Esquema import Esquema 
from Pagina import Pagina

class Tabela:
    def __init__(self, csv_path, table_name):
        self.table_name = table_name
        self.csv_path = csv_path
        # Quantidade de paginas na tabela
        self.pag_count = 0
        
        # Criamos o diretorio das paginas dessa tabela
        if(not os.path.exists("./" + self.table_name)):
            os.mkdir("./" + self.table_name)
        
        # Deleta as paginas antigas
        for i in os.listdir("./" + self.table_name):
            os.remove("./" + self.table_name + "/" + i)
            
    def carregarDados(self):
        with open(self.csv_path, 'r') as csvfile:
            reader = csv.reader(csvfile)

            # Analisa o header e cria o esquema
            self.header = next(reader)
            self.esquema = Esquema(len(self.header), dict(list(zip(self.header, range(len(self.header))))))
            
            # Carrega e salva os dados pagina por pagina
            pagina = Pagina()
            for row in reader:
                # Se a pagina esta cheia
                if(pagina.qtd_tuplas_ocup == 12):
                    # Salvamos a pagina cheia no disco
                    pagina.write("./{}/{}.txt".format(self.table_name, self.pag_count))
                    self.pag_count += 1

                    # Pegamos uma nova pagina vazia (a antiga é deletada)
                    pagina = Pagina()
                pagina.add(row)
            # Caso a ultima pagina possua dados (não salvos no disco, ainda)
            if(pagina.qtd_tuplas_ocup != 0): 
                pagina.write("./{}/{}.txt".format(self.table_name, self.pag_count))
                self.pag_count += 1
