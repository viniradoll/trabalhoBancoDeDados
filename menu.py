import os
from ClassesDeOperacao import Tabela
import ClassesDeDados

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
          self.tabela = Tabela(ClassesDeDados.Pedido)
        case 2:
          self.tabela = Tabela(ClassesDeDados.Produto)

    self.mainMenu()
    
  def select(self):
    os.system('cls')
    try:
      id = int(input("Informe o ID para busca: (0 para buscar todos)\n"))
    except:
      id = 0
    arr = self.tabela.select(id=id)
    for i in arr:
      print(i)

  def insert(self):
    arr = self.tabela.classeDados().retornaNomeAtributos()
    obj = {}
    os.system('cls')
    print("Informe os valores para os seguintes campos: (Deixe vazio para null)")
    for item in arr:
      print(f"{item}: ", end="")
      valor = input()
      if valor.isdigit():
        valor = int(valor)
      elif valor.replace('.','',1).isdigit() and valor.count('.') < 2:
        valor = float(valor)
      obj[item] = valor
        
    self.tabela.insert(obj)

  def update(self):
    os.system('cls')
    arr = self.tabela.classeDados().retornaNomeAtributos()
    print("Qual a coluna que deseja alterar?")

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
        self.select()
      case 2:
        self.insert()
      case 3:
        self.update()
      case 4:
        pass
