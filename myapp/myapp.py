
from flask import Flask, request, render_template
from . import myimg
from .myuser import User as MyUser
from . import getconfig
from .mylib import to_html

app = Flask(__name__)


@app.route('/')
def mymain():
    pag = f'''
    <h1>Pagina Inicial. Seja bem vindo</h1>
    <br><br>
    <a href="/novocadastro">Cadastre-se</a>
    <br><br>
    <p>Fim..</p>
    '''
    return pag


@app.route('/novocadastro')
def novocadastro():
    return render_template('novocadastro.html')


@app.route('/cadastro2', methods=['POST'])
def cadastro2():
  cfg = getconfig()
  mymap = cfg['mapping-html2attr']
  clsname = MyUser.__name__
  cfgmap = mymap[clsname]
  fromhtml = dict(request.form)

  diff = set(cfgmap) - set(fromhtml)  # verifica diferenca
  for key in diff:
    fromhtml[key] = request.files[key]

  params = {}
  for htmlattr, userattr in cfgmap.items():
    if htmlattr not in fromhtml:
      continue
    params[userattr] = fromhtml[htmlattr]

  obj = MyUser(**params)

  pag = f'''
  <h1>Cadastrando novo usuario...</h1>
  {to_html(obj)}
  '''
  return pag


@app.route('/cadastro', methods=['POST'])
def meu_cadastro():
    nome = request.form['usuario']
    login = request.form['login']
    email = request.form['email']
    senha = request.form['pwd']
    img = request.files['img']      # request.files.getlist('img')

    caminho = myimg.mysave(img)

    pag = f'''
    <h1>Voce digitou:</h1>
    <ul>
        <li>nome: {nome}</li>
        <li>email: {email}</li>
        <li>login: {login}</li>
        <li>senha: {senha}</li>
        <li>img: {caminho}</li>
        <img src="{caminho}">
    </ul>
    <h2>obrigado pela visita!</h2>
    '''
    return pag
