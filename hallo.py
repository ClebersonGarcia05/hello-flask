from flask import Flask

app = Flask(__name__)

@app.route('/')
def hallo():
    return '<h1>Hallo World</h1>'

if __name__ == '__main__':
    app.run()