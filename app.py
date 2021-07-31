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
    














if __name__ == '__main__':
    app.run(debug=True)
