from connection import conexao_DB
from os import system as sy
        
class Main():
    
    def __init__(self) -> None:
        pass
    
    def verificacao_sistema(self):
        if conexao_DB():
            print("Conexão com o database realizada ✅")
            return None
        else:
            print("Conexão com o database não concluida ❌")
            return False
    
    def main(self):
        sy("cls")
        if self.verificacao_sistema() == False:
            print("Sistema com problemas internos... ❌")
        else:
            print("\nSistema rodando... ✅")
    
Main().main()