
import logging
import unittest

class TesteMyTest(unittest.TestCase):
  def test_meutest0(self):
    logging.info('iniciando o testeeee... fazendo log...')
    print('iniciando o testeeeee....')


if __name__ == '__main__':
  logging.basicConfig(level=logging.INFO)
  # runner = unittest.TextTestRunner(verbosity=2)
  # unittest.main(testRunner=runner)
  unittest.main()
