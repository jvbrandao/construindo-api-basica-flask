from flask import Flask
from conselhos import Conselhos
from traducao import Traducao

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

cs = Conselhos()
tr = Traducao()

@app.route('/')
def root():
    return '<h1>documentação</h1>'

@app.route('/conselho')
def conselho():
    conselho = cs.conselho()
    return f"<h1>{conselho}</h1>"

@app.route('/tradutor/<idioma>/<frase>')
def traducao(idioma, frase):
    traducao = tr.traduzindo(f'{idioma}', f'{frase}')
    return f"<h1>{traducao}</h1>"

@app.route('/conselho-traduzido')
def conselho_traduzido():
    conselho = cs.conselho()
    traducao = tr.traduzindo('pt', f'{conselho}')
    return f"<h1>{traducao}</h1>"



app.run(debug=True)