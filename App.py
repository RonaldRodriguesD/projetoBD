from flask import Flask, render_template
from mongoengine import connect, Document, StringField, DateTimeField, ListField
app = Flask(__name__)
connect(host='mongodb+srv://admin:Ron.1807@cluster0.d1p1xsa.mongodb.net/test')
# criando uma rota com o decorator para a pagina inicial
@app.route("/")
def login():
    return render_template('login.html', title='Login', heading='Login', content='Faça login para acessar a aplicação')
@app.route("/home")
def home():
    return render_template('home.html', title='Home', heading='Home', content='Selecione a operação desejada')
