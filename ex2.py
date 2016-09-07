from flask import Flask
from flask import jsonify

app = Flask('pyladiessp')

@app.route('/pessoas')

def json_api():
    pessoas = [{"nome": "Bruno", "email": "bruno@email"},
               {'nome': "Arjen"},
               {"nome": "Anneke"},
               {"nome": "Steven"}]
    return jsonify(pessoas=pessoas, total=len(pessoas)), 200

app.run()
