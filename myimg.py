#!/usr/bin/python
# -*- coding: utf-8 -*-

import hashlib
import pathlib
import magic
import os


# as informacoes abaixo poderiam estar em uma configuracao...
BASE_APP_DIR = pathlib.Path.cwd()   # diretorio atual..
CAMINHO_PADRAO = 'static/imgs'      # onde salvar

mypath = BASE_APP_DIR.joinpath(CAMINHO_PADRAO)
if not mypath.exists():
    mypath.mkdir()

CAMINHO_PADRAO = str(mypath.resolve())
IMAGENS_ACEITAS = {'png', 'jpg', 'jpeg', 'gif'}
print('caminho padrao de imagens:', CAMINHO_PADRAO)
print('imagens aceitas:', IMAGENS_ACEITAS)


# Python Exception Hierarchy:
# https://docs.python.org/3/library/exceptions.html#exception-hierarchy
class MyImageError(ValueError):
    pass


def _get_buffer_extension(buffer):
    mimetype = magic.from_buffer(buffer.read(2048), mime=True)
    info = mimetype.rsplit('/')
    filetype = info[-1]
    return filetype



# from: https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/
def get_extension(buffer, fname):
    if not '.' in fname:
        extensao = _get_buffer_extension(buffer)
    else:
        nome_ext = fname.rsplit('.', 1)
        extensao = nome_ext[1]

    extensao = extensao.strip().lower()
    if not extensao in IMAGENS_ACEITAS:
        error_message = 'TIPO de arquivo desconhecido ou nao aceito!'
        raise MyImageError(error_message)

    return extensao


def get_imgname(img):
    ext = get_extension(img, img.filename)

    mybuff = repr(img).encode('utf-8')
    hash = hashlib.sha256(mybuff).hexdigest()
    imghash = str(hash)

    fname = f'{imghash}.{ext}'
    return fname


def mysave(img):
    img = redimensionar(img)
    fname = get_imgname(img)
    print(fname)

    fullpath = os.path.join(CAMINHO_PADRAO, fname)
    # img.save(fullpath)    # ainda nao estou salvando... 
    return fname


def redimensionar(img):
    return img


def mytest():
    with open('./static/imgs/marcelo-pereira.jpg', 'r') as myfile:
        print(myfile)

if __name__ == '__main__':
    mytest()
