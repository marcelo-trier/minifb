
import os
import json


def _update_items(orig, changelist):
    for key, value in changelist.items():
        print(f'mychange: {key} , {value}')
        klist = key.split(':')
        ultimo = klist.pop()
        ddtmp = orig

        while len(klist):
            subkey = klist.pop(0)
            ddtmp = ddtmp[subkey]

        ddtmp[ultimo] = value


def _update_config(cfg):
    # aqui setar todas configuracoes para cada profile...
    # caso necessario, sobrescrever as informacoes da configuracao atual...
    runcfg = cfg['run-config']
    runenv = runcfg['run-environment']
    cfg['run-environment'] = runenv

    changecfg = runcfg['environment-list'][runenv]
    _update_items(cfg, changecfg)

    runprofile = runcfg['run-profile']
    changecfg = runcfg['profile-list'][runprofile]
    _update_items(cfg, changecfg)


def _getconfig():
    basedir = os.path.dirname(__file__)
    cfgname = os.path.join(basedir, 'myconfig.json')

    with open(cfgname) as file:
        myconfig = json.load(file)

    myenv = dict(os.environ)
    _checkvalues(myconfig, myenv)

    myconfig['base-dir'] = basedir
    imgcfg = myconfig['image-config']
    path = os.path.join(basedir, imgcfg['img-path'])

    os.makedirs(path, exist_ok=True)
    print('img-path:', path)

    print('default image-path:', path)
    print('extensoes aceitas:', imgcfg['extensoes-aceitas'])

    _update_config(myconfig)

    return myconfig


def _checkvalues(element, myenv):
    if isinstance(element, list):
        for id in range(len(element)):
            element[id] = _checkvalues(element[id], myenv)

    if isinstance(element, dict):
        for k, v in element.items():
            element[k] = _checkvalues(v, myenv)

    if isinstance(element, str) and element.startswith('env:'):
        key = element[4:]
        element = myenv.get(key, '')

    return element


if __name__ == '__main__':
    mycfg = _getconfig()
    msg = json.dumps(mycfg, indent=4)
    print(msg)