from flask import  Flask, request, render_template
import json



app = Flask(__name__)

with open('./TPC5/conceitos.json', encoding='utf-8') as f:
    dados = json.load(f)


@app.route('/')
def conceitos():
    designacoes = list(dados.keys())

    return render_template("conceitos.html", designacoes=designacoes, title="Lista de Conceitos")


@app.route('/<designacao>')
def conceito_designacao(designacao):
    descricao = dados.get(designacao, "Não foi encontrada uma descrição")

    return render_template("palavra.html", designacao=designacao, descricao=descricao,title="Designação - Descrição")





app.run(host='localhost', port=4000, debug=True)