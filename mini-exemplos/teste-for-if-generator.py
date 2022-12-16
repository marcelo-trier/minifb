

dd = {
  'a': 1,
  'b': 2,
  'c': 3,
  '#--comment': 'nao imprimir',
  '--coment2': 'nao imprimir',
  'd': 4,
  'e': 5
}

# removendo comentarios que iniciam com '#' ou '--' ou '#--' ou '##'
dd = {k: v for k, v in dd.items() if not(k[0]=='#' or k[:2] in ('--', ))}
for key, value in dd.items():
  print(f'{key} -- {value}')
