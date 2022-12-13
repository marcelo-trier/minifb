
_mycfg = None

from .myuser import HtmlUser as MyUser


def getconfig():
    return _mycfg


def run():
    global _mycfg

    from .myconfig import _getconfig
    _mycfg = _getconfig()

    from .myapp import app
    runcfg = _mycfg['run-app']
    app.run(**runcfg)
