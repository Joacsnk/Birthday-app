from connection import conexao_DB
from os import system as sy
from time import sleep as sl
import questionary

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
        sl(3)
        sy("cls")
        self.selecionar_opcao()
        
    def interface(self):
        print('"_.~"~._.~"~._.~"~._.~"~._.~"~._.~"~._.~"~._.~"~._\n')
        print('                   BIRTHDAY APP                     ')
        print('\n"_.~"~._.~"~._.~"~._.~"~._.~"~._.~"~._.~"~._.~"~._\n')
        custom_style = questionary.Style([
                ("instruction", "hidden"),
        ])
        opcao = questionary.select(
            "",
            choices=[">>------> Adicionar aniversário", ">>------> Excluir aniversário", 
                     ">>------> Pesquisar aniversário", ">>------> Sair"],
            instruction=None,
            qmark="",
            style=custom_style
            
        ).ask()
        return opcao
        
    def selecionar_opcao(self):
        match self.interface():
            case ">>------> Sair":
                sy("cls")
                print("Programa encerrado com sucesso ✅")
                exit()
        
            

sl(3)
Main().main()