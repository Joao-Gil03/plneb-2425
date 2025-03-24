from flask import Flask, request, render_template, redirect
import json
app = Flask(__name__)

#db_file = open("../Aula4/conceitos.json")
db_file = open("conceitos_.json")

db = json.load(db_file)
db_file.close()

@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/conceitos")
def conceitos():
    designacoes = sorted(list(db.keys()))
    return render_template("conceitos.html", designacoes=designacoes, title="Lista de Conceitos")



@app.get("/conceitos/<designacao>")
def conceito(designacao):
    if designacao in db:
        return render_template("conceito.html",designacao=designacao, descricao=db[designacao])
    else:
        return render_template("conceito.html",designacao="Erro", descricao=" Descrição não encontradda")
    
    
@app.route("/api/conceitos")
def api_conceitos():
    return db

@app.route("/api/conceitos/<designacao>")
def api_conceito(designacao):

    return {"designacao":designacao, "descricao":db[designacao]}

@app.post("/conceitos")
def adiconar_conceito():
    descricao=request.form.get("descricao")
    designacao=request.form.get("designacao")
    
    db[designacao] = descricao
    f_out = open("conceitos_.json", "w", encoding="UTF-8")
    json.dump(db,f_out, indent=4, ensure_ascii=False)
    f_out.close()
    #form data
    
    designacoes = sorted(list(db.keys()))
    return render_template("conceitos.html",designacoes=designacoes, title="Lista de Conceitos")

@app.post("/api/conceitos")
def adicionar_conceito_api():
    #json
    data = request.get_json()
    #{"designacao":"vida", "descricao": "a vida é ..."}
    db[data["designacao"]] = data["descricao"]
    f_out = open("conceitos_.json", "w")
    json.dump(db,f_out, indent=4, ensure_ascii=False)
    f_out.close()
    #form data
    return data

@app.route("/pesquisa")
def pesquisa():

    termo = request.args.get('termo', '')
    palavra_inteira = request.args.get('palavra_inteira', 'off') == 'on'
    if termo:
        
        return redirect(f"/pesquisa/{termo}?palavra_inteira={'on' if palavra_inteira else 'off'}")
    
    return render_template("pesquisa.html", title="Pesquisa")

@app.route("/pesquisa/<termo>")
def r_pesquisa(termo):
    palavra_inteira = request.args.get('palavra_inteira', 'off') == 'on'
    if palavra_inteira:
        resultados = [designacao for designacao in db.keys() if termo.lower() == designacao.lower()]
    else:
        resultados = [designacao for designacao in db.keys() if termo.lower() in designacao.lower()]
    return render_template("r_pesquisa.html", termo=termo, resultados=resultados, title="Resultados da Pesquisa")

app.run(host="localhost", port=4002, debug=True)
