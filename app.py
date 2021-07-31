from flask import Flask, render_template, redirect, request

app = Flask(__name__)

acesso_usuario = 'admin'
acesso_senha = "admin"

class Login:
    
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
        

@app.route('/')
def index():
    return render_template('index.html')


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
        return redirect('/') #Fazer interação de acesso negado com JS
    

@app.route('/about')
def page_about():
    return render_template('sobre.html')

@app.route('/loja')
def page_loja():
    return render_template('loja.html')

#Fiz as rotas para os outros botões, mas acredito que seja desnecessário, essa parte pode ficar só no FRONT










if __name__ == '__main__':
    app.run(debug=True)
