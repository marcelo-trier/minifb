
_mycfg = None


def getconfig():
    return _mycfg


def run():
    global _mycfg
    from .config.myconfig import MYCONFIG
    cfg = MYCONFIG()
    _mycfg = cfg.load()

    from .myapp import app
    runcfg = _mycfg['run-app']
    app.run(**runcfg)
