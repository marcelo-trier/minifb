
from myapp.bancodados import BancoDados

import unittest


class TestBancoDados(unittest.TestCase):
  def test_bdconnection(self):
    print('\nStart testing database connection..')
    obj = BancoDados()
    obj.conectar()
    df = obj.executar_sql('SHOW TABLES')
    print(df)
    tabbanco = set(df[df.columns[0]])
    tabcompara = ['tbAmigo', 'tbMensagem', 'tbUsuario']
    self.assertEqual(tabbanco, set(tabcompara))



if __name__ == '__main__':
  unittest.main(verbosity=2)

