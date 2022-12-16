
from myapp.config.myconfig import MYCONFIG
import unittest

class TestConfiguracao(unittest.TestCase):
  def test_config(self):
    mycfg = MYCONFIG()
    mycfg.load()
    print(mycfg)




if __name__ == '__main__':
  unittest.main(verbosity=2)

