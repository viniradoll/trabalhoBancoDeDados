import os
from ClassesDeOperacao import Tabela
from ClassesDeDados import Pedido, Produto

class Menu:

  tabela = None

  def __init__(self):
    while(self.tabela == None):
      os.system('cls')
      print("Qual tabela deseja acessar?\n")
      print("(1) pedidos")
      print("(2) produtos")
      try:
        val = int(input("\n"))
      except:
        val = 0

      match val:
        case 1:
          self.tabela = Tabela(Pedido)
        case 2:
          self.tabela = Tabela(Produto)

    self.mainMenu()
        

  def mainMenu(self):
    val = 0
    while (val not in [1, 2, 3, 4]):
      os.system('cls')
      print("Qual operação deseja realizar?\n")
      print("(1) Select")
      print("(2) Insert")
      print("(3) Update")
      print("(4) Delete")
      try:
        val = int(input("\n"))
      except:
        val = 0
      
    match val:
      case 1:
        print(self.tabela.select())
      case 2:
        pass
      case 3:
        pass
      case 4:
        pass




a = Menu()