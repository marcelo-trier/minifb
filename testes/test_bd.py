
from myapp.bancodados import BancoDados

import unittest


class TestBancoDados(unittest.TestCase):
  def test_bdconnection(self):
    print('\nStart testing database connection..')
    obj = BancoDados()
    obj.conectar()
    df = obj.executar_sql('SHOW TABLES')
    print(df)
    ll = df[df.columns[0]].tolist()
    l2 = ['tbAmigo', 'tbMensagem', 'tbUsuario']
    print('tabelas:', ll)



if __name__ == '__main__':
  unittest.main(verbosity=2)

