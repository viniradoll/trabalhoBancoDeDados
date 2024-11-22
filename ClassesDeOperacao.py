import mysql.connector
from ClassesDeDados import Produto, Pedido

class BancoDados:
  conexao = None
  
  # conexão:
  def __conectar__(self):
    if self.conexao == None or not self.conexao.is_connected():
      self.conexao = mysql.connector.connect(
        user = 'administrativo',
        password = 'adm',
        host = 'localhost',
        database = 'sorveteria'
    )
    return self.conexao.cursor()
     
 
  def __desconectar__(self):
    if self.conexao != None and self.conexao.is_connected():
      self.conexao.disconnect()
  ########################
  
class Tabela(BancoDados):
  # dataClass é uma referencia para uma classe (NÃO UM OBJETO!)
  def __init__(self, dataClass: type):
      self.tabela = dataClass.tabela
      self.classeDados = dataClass

  def select(self, id: int = 0, customWhere: str = None) -> list:
    cursor = self.__conectar__()

    sql =  self.classeDados().retornaSelect()
    if (id > 0): sql += f' where id = {id}'
    elif (customWhere is not None): sql += f' {customWhere}'
    print(sql)
    cursor.execute(sql)
    retorno = self.criarResultSet(cursor)

    self.__desconectar__()
    return retorno

  def criarResultSet(self,cursor):
    Array = []
    for linha in cursor:
      Obj = self.classeDados()
      campos = Obj.retornaNomeAtributos()
      for i, val in enumerate(linha):
         setattr(Obj,campos[i],val)
      Array.append(Obj)
    return Array


class Tabela_Pedidos(BancoDados):
  def getPedidos(self):
    cursor = self.__conectar__()
    cursor.execute("select id, nomeComprador, valorTotal, dataHoraPedido from pedidos")
    pedidos = []
    for linha in cursor:
      pedidos.append(
        Pedido(
          id = linha[0],
          nomeComprador = linha[1],
          valorTotal = linha[2],
          dataHoraPedido = linha[3]
        )
      )
    self.__desconectar__()
    return pedidos
     
  def getPedido(self, id: int):
    cursor = self.__conectar__()
    cursor.execute(
      "select id, nomeComprador, valorTotal, dataHoraPedido from pedidos \
       where id=%s", [id])
    pedido = None
    for linha in cursor:
      pedido = Pedido(
        id = linha[0],
        nomeComprador = linha[1],
        valorTotal = linha[2],
        dataHoraPedido = linha[3]
      )
    self.__desconectar__()
    return pedido
  
class Tabela_Produtos(BancoDados):
    def getProdutos(self):
        cursor = self.__conectar__()
        cursor.execute("select id, descricao, quantidade, valorUnidade, idReceita from produtos")
        produtos = []
        for linha in cursor:
            produtos.append(
                Produto(
                id = linha[0],
                descricao=linha[1],
                quantidade = linha[2],
                valorUnidade = linha[3],
                idReceita = linha[4]
                )
            )
        self.__desconectar__()
        return produtos
        
    def getProduto(self, id: int):
        cursor = self.__conectar__()
        cursor.execute(
            "select id, descricao, quantidade, valorUnidade, idReceita from produtos \
            where id=%s", [id])
        produto = None
        for linha in cursor:
            produto = Produto(
                id = linha[0],
                descricao=linha[1],
                quantidade = linha[2],
                valorUnidade = linha[3],
                idReceita = linha[4]
            )
        self.__desconectar__()
        return produto