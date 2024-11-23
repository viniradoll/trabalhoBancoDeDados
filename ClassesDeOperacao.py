import mysql.connector

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
  
  def __commit__(self):
    self.conexao.commit()
 
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


  def insert(self, obj: dict):
    cursor = self.__conectar__()

    campos = ""
    valores = ""
    for key, val in obj.items():
      if val == "": continue
      campos += key + ", "
      if not isinstance(val, (int, float)):
        val = "'" + str(val) + "'"
      valores += str(val) + ", "
    
    sql = f"INSERT INTO {self.tabela} ({campos[:-2]}) VALUES ({valores[:-2]})"
    cursor.execute(sql)
    self.__commit__()
    print(cursor.rowcount, " linha(s) afetada(s)")
    self.__desconectar__()
  
  def update(self, id:int, obj:dict, customWhere = ""):
    cursor = self.__conectar__()

    sql = f"UPDATE {self.tabela} SET "
    for key, val in obj.items():
      if val == "": continue
      if not isinstance(val, (int, float)):
        val = "'" + str(val) + "'"
      sql += f"{str(key)} = {str(val)}, "
    sql = sql[:-2]
    if customWhere == "":
      sql += f" WHERE ID = {id}"
    else:
      sql += f"WHERE {customWhere}"

    cursor.execute(sql)
    self.__commit__()
    print(cursor.rowcount, " linha(s) afetada(s)")
    self.__desconectar__()

  def delete(self, id, customWhere = ""):
    cursor = self.__conectar__()
    sql = f"DELETE FROM {self.tabela} WHERE "
    if customWhere == "":
      sql += f"ID = {id}"
    else:
      sql += customWhere
    
    cursor.execute(sql)
    self.__commit__()
    print(cursor.rowcount, " linha(s) afetada(s)")
    self.__desconectar__()