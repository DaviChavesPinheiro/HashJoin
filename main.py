from HashEstatico import HashEstatico
from Tabela import Tabela
from Operador import Operador
import os

def main():
    vinho = Tabela("vinho.csv", "Vinho") # cria estrutura necessaria para a tabela
    uva = Tabela("uva.csv", "Uva")
    pais = Tabela("pais.csv", "Pais")
    
    vinho.carregarDados() # le os dados do csv e add na estrutura da tabela, caso necessario
    uva.carregarDados()
    pais.carregarDados()

    # op = Operador(vinho, pais, "pais_producao_id", "pais_id")
    # op = Operador(uva, pais, "pais_origem_id", "pais_id")
    op = Operador(vinho, uva, "uva_id", "uva_id")

    join_prefix = op.executar() # Realiza a operacao desejada

    print("#Pags:", op.numPagsGeradas) # Retorna a quantidade de paginas geradas pela operacao
    print("#Tups:", op.numTuplasGeradas) # Retorna a quantidade de tuplas geradas pela operacao
    print("#IOss:", op.numIOExecutados) # Retorna a quantidade de IOs geradas pela operacao

    op.salvarTuplasGeradas(join_prefix) # Retorna as tuplas geradas pela operacao e salva em um csv

# Limpa alguns diretorios antes de inicializar o programa
def limpa_pastas():
    if (os.path.exists("./join")):
        # deleta as paginas antigos
        for i in os.listdir("./join"):
            os.remove("./join/" + i)
limpa_pastas()
main()
