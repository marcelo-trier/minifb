#!/usr/bin/python
# -*- coding: utf-8 -*-

import hashlib
import magic
import os
from . import getconfig
from PIL import Image


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
    cfg = getconfig()
    imgcfg = cfg['image-config']
    extensoes = imgcfg['extensoes-aceitas']

    if not '.' in fname:
        extensao = _get_buffer_extension(buffer)
    else:
        nome_ext = fname.rsplit('.', 1)
        extensao = nome_ext[1]

    extensao = extensao.strip().lower()
    if not extensao in extensoes:
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
    cfg = getconfig()
    imgcfg = cfg['image-config']
    imgpath = imgcfg['img-path']

    fname = get_imgname(img)
    img = redimensionar(img)
    fullpath = os.path.join(imgpath, fname)
    print('imagem:', img)
    
    if imgcfg['save-image']:
        print('salvando:', fname)
        img.save(fullpath)

    return fname


def redimensionar(img):
    # from: https://cloudinary.com/guides/bulk-image-resize/python-image-resize-with-pillow-and-opencv
    cfg = getconfig()
    imgcfg = cfg['image-config']
    mw = imgcfg['max-width']
    mh = imgcfg['max-height']

    myimg = Image.open(img)
    (w, h) = myimg.size
    print('image size (orig):', (w,h))
    print(f'max img size - width:{mw}, height:{mh}')

    if w > mw or h > mh:
        myimg.thumbnail( (mw, mh) )
        print('image size (resized):', myimg.size)

    # ver tbem:
    # https://opensource.com/life/15/2/resize-images-python
    # https://auth0.com/blog/image-processing-in-python-with-pillow/
    return myimg


def mytest():
    with open('./static/imgs/marcelo-pereira.jpg', 'r') as myfile:
        print(myfile)

if __name__ == '__main__':
    mytest()
