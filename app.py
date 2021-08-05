from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ilzpkagm:tFfCmwORirxRZeVpvqJJ1vFd7YVWXOE6@kesavan.db.elephantsql.com/ilzpkagm'
acesso_usuario = 'admin'
acesso_senha = 'admin'

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
    preco = db.Column(db.Float(40), nullable = False )
    # categoria = db.Column(db.String(20), nullable = False)
    
    def __init__(self, nome,descricao,imagem,preco):
        self.nome = nome
        self.descricao = descricao
        self.imagem = imagem
        self.preco = preco
        # self.categoria = categoria


# Página de Login do ADM
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')    
def login():
    return render_template('login.html')

@app.route('/voltar')
def volta_pagina():
    return render_template('index.html')

# Validação de user e password para entrada na área do ADM
@app.route('/admin', methods = ['GET','POST'])
def admin():
    if request.method == 'POST':
        login = Login(
            request.form['username'],
            request.form['password']
        )
    
    if login.usuario and login.senha == acesso_usuario and acesso_senha:
        # pagina_vendedor = Vendedor.query.All()
        return render_template('admin.html')
    else: 
        return render_template('login.html')
    


# CRUD- Fazendo o CREATE

@app.route('/formulario', methods = ['GET', 'POST'])
def new_form():
    if request.method == 'POST':
        produto = Vendedor(
            request.form['nome'],
            request.form['descricao'],
            request.form['imagem'],
            request.form['preco']
            # ,request.form['categoria']
        )
    db.session.add(produto)
    db.session.commit()
    pagina_vendedor = Vendedor.query.All()
    return render_template('admin.html' , tabela=pagina_vendedor)
@app.route('/add', methods = ['POST', 'GET'])
def add_item():
    
    return render_template('add.html')



@app.route('/loja')
def pagina_loja():
    return render_template('loja.html')

@app.route('/about')
def pagina_sobre():
    return render_template('sobre.html')







#testando essa bagaça!!!!!!



if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
