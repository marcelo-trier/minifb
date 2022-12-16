
from mysql import connector
import pandas as pd
from myapp import getconfig


class BancoDados:
  def __init__(self):
    self.mydb = None
    self.conexao = None

  def conectar(self):
    cfg = getconfig()
    dbconfig = cfg['database-config']
    self.mydb = connector.connect(**dbconfig)
    self.conexao = self.mydb.cursor()

  def executar_sql(self, sql):
    self.conexao.execute(sql)
    table_rows = self.conexao.fetchall()
    colunas = self.conexao.column_names
    df = pd.DataFrame(table_rows, columns=colunas)
    return df



