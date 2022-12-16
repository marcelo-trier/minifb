
_mycfg = None
_banco = None

def getconfig():
  global _mycfg
  from .config.myconfig import MYCONFIG
  if not _mycfg:
    cfg = MYCONFIG()
    _mycfg = cfg.load()
  return _mycfg


def run():
    global _banco
    #_banco = iniciarbanco()
    cfg = getconfig()
    runcfg = cfg['run-app']

    from .myapp import app
    app.run(**runcfg)
