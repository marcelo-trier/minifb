
import os
import json
from mergedeep import merge


class MYCONFIG:
  def __init__(self, fname='myconfig.json'):
    self._fname = fname
    path = os.path.abspath(__file__)
    self._path = os.path.dirname(path)
    self._config = None
    self._environment = None

  def fullname(self, fname=None):
    if not fname:
      fname = self._fname
    return os.path.join(self._path, fname)

  @property
  def config(self):
    return self._config


  def __str__(self):
    msg = f'''
      CONFIGURACAO ATUAL:
      -- fname: {self._fname}
      -- path: {self._path}
      -- CONFIG: 
      {json.dumps(self._config, indent=4)}
    '''
    return msg

  def load(self):
    fname = self.fullname()
    with open(fname) as file:
        cfg = json.load(file)

    for fname in cfg.get('import-files', ''):
      fname = self.fullname(fname)
      with open(fname) as file:
        cfg2 = json.load(file)
      cfg = merge(cfg, cfg2)


    self._environment = dict(os.environ)      # capturando as configuracoes do 'environment'
    self._config = self._checkenv(cfg)

    # diretorio base serah um diretorio anterior da configuracao, pois a configuracao estah em: ./config/myconfig.py
    dirback = os.path.join(self._path, '..')  
    os.chdir(dirback)
    basedir = os.getcwd()
    self._config['base-dir'] = basedir        # diretorio base do myapp, um diretorio anterior ou acima da configuracao
    imgcfg = self._config['image-config']
    imgpath = os.path.join(basedir, imgcfg['img-path'])

    os.makedirs(imgpath, exist_ok=True)
    print('default img-path:', imgpath)
    print('extensoes aceitas:', imgcfg['extensoes-aceitas'])
    return self._config

  # funcao recursiva... ;o)
  def _checkenv(self, element):
    if isinstance(element, dict):
      for key, value in element.items():
        element[key] = self._checkenv(value)

    if isinstance(element, list):
        for id in range(len(element)):
            element[id] = self._checkenv(element[id])

    if isinstance(element, str) and element.startswith('env:'):
      key = element[4:]
      element = self._environment.get(key, '')

    return element





if __name__ == '__main__':
  mycfg = MYCONFIG()
  mycfg.load()
  print(mycfg)
