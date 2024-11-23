class DadosBase:
  tabela = None
  
  def __iter__(self):
    for attr, value in self.__dict__.items():
      yield attr, value  

  def __repr__(self):
    Str = ""
    for key, val in self:
      Str += f'{key}: {val}   '
    return Str[:-3]
  
  def retornaNomeAtributos(self):
    array = []
    for i in self:
      array.append(i[0])
    return array

  def retornaCamposSql(self):
    array = self.retornaNomeAtributos()
    return str(array)[1:-1].replace("'", "")
  
  def retornaSelect(self):
    return f'select {self.retornaCamposSql()} from {self.tabela}'
  


class Pedido(DadosBase):
  
  tabela = "pedidos"
  id = None
  nomeComprador = None
  valorTotal = None
  dataHoraPedido = None

  def __init__(self, id = None, nomeComprador = None, valorTotal = None, dataHoraPedido = None):
    self.id = id
    self.nomeComprador = nomeComprador
    self.valorTotal = valorTotal
    self.dataHoraPedido = dataHoraPedido


class Produto(DadosBase):
  
  tabela = "produtos"
  id = None
  descricao = None
  quantidade = None
  valorUnidade = None
  idReceita = None

  def __init__(self, id = None, descricao = None, quantidade = None, valorUnidade = None, idReceita = None):
    self.id = id
    self.descricao = descricao
    self.quantidade = quantidade
    self.valorUnidade = valorUnidade
    self.idReceita = idReceita