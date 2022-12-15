
def to_html(obj):
  attr = vars(obj)       # captura todos atributos
  lista = [f'<li>{attr}: {vlr}</li>' for attr,
            vlr in attr.items()]   # dict comprehension
  html = '\n'.join(lista)
  pag = f'''
  <ul>
    {html}
  </ul>
  '''
  return pag


# @classmethod
# def fromhtml(cls, request):
#   values = dict(request.form)

#   flist = request.files.getlist('img')
#   buffer = flist[0]        # capturando somente a primeira imagem..
#   fname = myimg.mysave(buffer)
#   values['img'] = fname

#   params = {}
#   for html, usr in cls.mapeamento.items():
#     if html not in values:
#       continue
#     params[usr] = values[html]

#   obj = cls(**params)
#   return obj
