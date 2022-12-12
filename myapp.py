
from flask import Flask, request, render_template
import myimg
import myuser

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
    return render_template('teste-form.html')


@app.route('/cadastro2', methods=['POST'])
def cadastro2():
    user = myuser.HtmlUser.fromhtml(request)

    pag = f'''
    <h1>Cadastrando novo usuario...</h1>
    {user.tohtml()}
    '''
    return pag


@app.route('/cadastro', methods=['POST'])
def meu_castro():
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


if __name__ == '__main__':
   app.run(debug=True, use_debugger=False, use_reloader=False)
   # app.run()
