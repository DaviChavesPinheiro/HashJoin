# Classe que garante que apenas uma página está sendo carregada na memória por vez
class Page:
    data = []
    
    def __init__(self):
        pass

    @staticmethod
    def read(path): 
        with open(path, 'r') as f:
            Page.data = f.readlines()
    @staticmethod
    def write(path): 
        with open(path, 'w') as f:
            f.writelines(Page.data)
     
 
