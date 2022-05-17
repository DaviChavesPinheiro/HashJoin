import uuid
import os
import csv
from HashEstatico import HashEstatico
from Pagina import Pagina

class Operador:
    def __init__(self, table1, table2, col1, col2):
        self.table1 = table1
        self.table2 = table2
        self.col1 = col1
        self.col2 = col2

        # Se a pasta dos joins ainda não existir, ela é criada
        if (not os.path.exists("./join")):
            os.mkdir("./join")

    def executar(self):
        # Prefixo dos arquivos desse join
        prefix = str(uuid.uuid4())

        # Quantidade de paginas (txt) escritas
        pag_count = 0

        hashEstatico = HashEstatico(5)
        
        # Para cada página da tabela 1
        for i in range(self.table1.pag_count):
            # Leia uma pagina
            pagina = Pagina()
            pagina.read("{}/{}.txt".format(self.table1.table_name, i))
            
            # Adiciona cada tupla no indice
            for tupla in pagina.tuplas:
                # Pega a coluna que vai servir de indice
                col = tupla.cols[self.table1.esquema.nome_para_indice[self.col1]]
               
                hashEstatico.add(col, ",".join(tupla.cols)) 
            # Referencia da pagina deletada
            del pagina
        
        # Página que vai armazenar o join
        join_pagina = Pagina()
        # Para cada página da tabela 2
        for i in range(self.table2.pag_count):
            # Leia uma pagina
            pagina = Pagina()
            pagina.read("{}/{}.txt".format(self.table2.table_name, i))
            
            for tupla2 in pagina.tuplas:
                # Pega a coluna que vamos usar para procurar no indice
                col = tupla2.cols[self.table2.esquema.nome_para_indice[self.col2]]
            
                # TODO: iterador?
                tuplas1 = hashEstatico.find(col)
                for tupla1 in tuplas1:
                    # Se a pagina de join esta cheia
                    if(join_pagina.qtd_tuplas_ocup == 12):
                        # Escrevemos o join em um txt
                        join_pagina.write2("./join/{}-{}.txt".format(prefix, pag_count))
                        pag_count += 1

                        # Referencia da pagina deletada
                        del join_pagina
                        # Nova página criada
                        join_pagina = Pagina()
                    join_pagina.add(tupla1 + "," + ",".join(tupla2.cols))
                
            # Caso a ultima pagina possua dados (não salvos no disco, ainda)
            if(join_pagina.qtd_tuplas_ocup != 0): 
                join_pagina.write2("./join/{}-{}.txt".format(prefix, pag_count))
                pag_count += 1

            # Referencia da página deletada        
            del pagina        
        # Referencia do join deletada
        del join_pagina
        return prefix
            
    def salvarTuplasGeradas(self, prefix):
        path = "{}_{} X {}_{} ({}).csv".format(self.table1.table_name, self.col1, self.table2.table_name, self.col2, prefix)

        with open(path, "w") as f:
            writer = csv.writer(f)
            # Escreve o header do csv
            writer.writerow(self.table1.header + self.table2.header)
            
            # Percorre todas as páginas de join
            if (os.path.exists("./join")):
                for page_name in os.listdir("./join"):
                    # Caso o arquivo comece com o prefixo
                    if(page_name.startswith(prefix)):
                        pagina = Pagina()
                        pagina.read("./join/{}".format(page_name))

                        writer.writerows(list(map(lambda tupla: tupla.cols, pagina.tuplas)))
                        del pagina


            



