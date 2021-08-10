from flask import Flask, render_template, redirect, request, session,flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://oylvfkns:gWSc41l04bs7TG30DKBPzTEl7eJB_Bnp@kesavan.db.elephantsql.com/oylvfkns'
acesso_usuario = 'admin'
acesso_senha = 'admin'
app.secret_key = 'store'

#Classe que recebe o usuário e senha dos donos do Site.
class Login():
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
# Classe que cria a table
class Vendedor(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement = True )
    nome = db.Column(db.String(50), nullable= False)
    descricao = db.Column(db.String(500), nullable =False)
    imagem = db.Column(db.String(7000), nullable=False)
    preco = db.Column(db.Integer, nullable = False )
    def __init__(self, nome,descricao,imagem,preco):
        self.nome = nome
        self.descricao = descricao
        self.imagem = imagem
        self.preco = preco
# Página princial
# e principais rotas
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/loja')
def pagina_loja():
    return render_template('loja.html')
@app.route('/about')
def pagina_sobre():
    return render_template('sobre.html')
@app.route('/login')    
def login():
    session['usuario_logado'] = None
    return render_template('login.html')
# aqui acabam as rotas principais

# Rotas de autentição
@app.route('/auth', methods = ['GET', 'POST'])
def auth():
    if request.method == 'POST':
            login = Login(
                request.form['username'],
                request.form['password']
            )
    if login.usuario and login.senha == acesso_usuario and acesso_senha:
        session['usuario_logado'] = 'admin'
        flash('login efetuado')
        return redirect('/admin')
    else:
        flash('Erro no login, tente novamente!')
        return redirect('/login') 

@app.route('/voltar')
def home():
    return redirect('/')

@app.route('/admin', methods = ['GET','POST'])
def admin():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        flash('Faça o login antes de entrar nessa rota!')
        return redirect('/login') 
    tabelas = Vendedor.query.all()
    return render_template('admin.html', tabelas=tabelas, produto='') 
  
@app.route('/logout')
def volta_pagina():
    session['usuario_logado'] = None
    return render_template('login.html')
# aqui terminam as toras de altentição


@app.route('/admin', methods = ['GET','POST'])
def admin():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        flash('Faça o login antes de entrar nessa rota!')
        return redirect('/login') 
    tabelas = Vendedor.query.all()
    return render_template('admin.html', tabelas=tabelas, produto='') 
  
@app.route('/logout')
def volta_pagina():
    session['usuario_logado'] = None
    return render_template('login.html')
# aqui terminam as toras de altentição


# aqui começam as rotas de manipulação do banco de dados
# CRUD- Fazendo o CREATE
@app.route('/select')
def selected():
    tabelas = Vendedor.query.all()
    return render_template('/admin.html', tabelas=tabelas, produto='', display='true')    

@app.route('/new', methods = ['GET', 'POST'])
def new_form():
    if request.method == 'POST':
        produto = Vendedor(
            request.form['nome'],
            request.form['descricao'],
            request.form['imagem'],
            request.form['preco']
        )

    db.session.add(produto)
    db.session.commit()
    tabelas = Vendedor.query.all()
    return render_template('/admin.html', display='',tabelas=tabelas, produto='')


@app.route('/edit/<id>', methods=['GET', 'POST'])
def edita_item(id):
    produto = Vendedor.query.get(id)
    tabelas = Vendedor.query.all()
    if request.method == "POST":
        produto.nome = request.form['nome']
        produto.descricao = request.form['descricao']
        produto.imagem = request.form['imagem']
        produto.preco = request.form['preco']
        db.session.commit() 
        return redirect('/admin')
    return render_template('admin.html', display='true', tabelas=tabelas, produto=produto) 


@app.route('/<id>')
def idselector(id):
    produto = Vendedor.query.get(id)
    tabelas = Vendedor.query.all()
    return render_template('admin.html', select=produto, tabelas=tabelas, produto='')


@app.route('/delete/<id>')
def delete(id):
    produto = Vendedor.query.get(id)
    db.session.delete(produto)
    db.session.commit()
    return redirect('/admin')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
