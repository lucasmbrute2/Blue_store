from flask import Flask, render_template, redirect, request, session,flash
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ilzpkagm:tFfCmwORirxRZeVpvqJJ1vFd7YVWXOE6@kesavan.db.elephantsql.com/ilzpkagm'
acesso_usuario = 'admin'
acesso_senha = 'admin'
app.secret_key = 'store'

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
@app.route('/new_item')
def item():
    return render_template('new_item.html',produto ='')



@app.route('/voltar')
def home():
    return redirect('/')


@app.route('/admin', methods = ['GET','POST'])
def admin():
    # if 'usuario_logado' not in session or session['usuario_logado'] == None:
    #     flash('Faça o login antes de entrar nessa rota!')
    #     return redirect('/login') 
    tabelas = Vendedor.query.all()
    return render_template('admin.html', tabelas=tabelas, produto='') 
    
# Rotas de autentição
@app.route('/autenticar', methods=['GET', 'POST'])
def auth_login():
    if request.method =='POST' and request.form['password'] == 'admin':
        session['user_logado'] = 'logado'
        flash('Login feito com sucesso!')
        return redirect('/admin')
    else:
        flash('Usuário ou senha inválida, digite novamente.')
        return render_template('login.html')



@app.route('/logout')
def volta_pagina():
    session['usuario_logado'] = None
    return render_template('login.html')
# aqui terminam as toras de altentição


# aqui começam as rotas de manipulação do banco de dados
# CRUD- Fazendo o CREATE
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
        return redirect('/admin')

#CRUD -Fazendo o EDIT

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
    return render_template('admin.html', tabelas=tabelas, produto=produto) 


@app.route('/<id>')
def idselector(id):
    produto_del = Vendedor.query.get(id)
    return render_template('admin.html', produto_del=produto_del, produto ='')


@app.route('/delete/<id>')
def delete(id):
    produto = Vendedor.query.get(id)
    db.session.delete(produto)
    db.session.commit()
    return redirect('/admin')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
