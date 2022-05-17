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
    op = Operador(vinho, uva, "uva_id", "uva_id")

    join_prefix = op.executar() # Realiza a operacao desejada
    return 
    # TODO: TENTAR UTIZAR APENAS UMA CLASSE PAGINA DE LOADING??? COLOCAR UMA VARIAVEL ESTATICA PARA CONTAR QUANTAS PAGINAS FORAM CARREGADAS
    # TODO: FAZER numPagsGeradas numIOExecutados numTuplasGeradas
    # TODO: SALVAR NO CSV
    # TODO: CONFIRIR SE SOMENTE NO MAXIMO 3 PAGINAS ESTÃO SENDO CARREGAS NA MEMORIA POR VEZ
    print("#Pags:", op.numPagsGeradas()) # Retorna a quantidade de paginas geradas pela operacao
    print("#IOss:", op.numIOExecutados()) # Retorna a quantidade de IOs geradas pela operacao
    print("#Tups:", op.numTuplasGeradas()) # Retorna a quantidade de tuplas geradas pela operacao
    
    op.salvarTuplasGeradas("selecao_vinho_ano_colheita_1990.csv") # Retorna as tuplas geradas pela operacao e salva em um csv

# Limpa alguns diretorios antes de inicializar o programa
def limpa_pastas():
    if (os.path.exists("./join")):
        # deleta as paginas antigos
        for i in os.listdir("./join"):
            os.remove("./join/" + i)
limpa_pastas()
main()
