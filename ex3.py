from flask import Flask, request, render_template

app = Flask("wtf")

@app.route('/noticias/<pais>')
def lista_de_noticias(pais):
    cat = request.args.get('categoria')
    qtd = request.args.get('')
