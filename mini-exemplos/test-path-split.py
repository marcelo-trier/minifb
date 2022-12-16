
# ref: https://www.geeksforgeeks.org/python-os-path-split-method/

import os


mytests = [
  '/home/user/file.txt',
  '/home/user/',
  '/home/user',     # aqui vai dar erro! o Py vai achar que 'user' eh um arquivo, pois a string toda nao termina com '/'
  'file.txt',
  ''
]

def show_path(value):
  print(f'## processando valor: {value}')
  (path, file) = os.path.split(value)
  print(f'    dir: {path} , file: {file}')

  notpath = ''
  notfile = ''
  if not path:
    notpath = '**NAO**'

  if not file:
    notfile = '**NAO**'

  print(f'    ...aqui o PATH {notpath} existe')
  print(f'    ...aqui o FILE {notfile} existe', end='\n\n')


for value in mytests:
  show_path(value)

