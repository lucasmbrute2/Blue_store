from flask import Flask, render_template, redirect, request

app = Flask(__name__)

acesso_usuario = 'admin'
acesso_senha = "admin"

class Login:
    
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
        
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
        return render_template('admin.html')
    else: 
        return render_template('login.html') #Fazer interação de acesso negado com JS
    
# Botões da página inicial
@app.route('/loja')
def pagina_loja():
    return render_template('loja.html')

@app.route('/about')
def pagina_sobre():
    return render_template('sobre.html')






# vai logo desgraça






if __name__ == '__main__':
    app.run(debug=True)
