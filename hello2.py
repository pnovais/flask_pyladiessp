from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
@app.route('/hello/<user>')
def hello_world(user=None):
    user = user or 'Shalabh'
    return '''
    <html>
        <head>
            <title> Templating in
            Flask</title>
        </head>
        <body>
        <h1>Hello %s </h1>
        <p> Welcome to the world of Flask</p>
        </body>
    </html>''' % user

if __name__ == '__main__':
    app.run()
