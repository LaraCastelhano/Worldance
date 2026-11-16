from flask import Flask

from database import init_db

app = Flask(__name__)

init_db()


@app.route("/", methods=["GET"])
def pagina_inicial():
    return "Bem vindo ao Worldance!"


if __name__ == "__main__":
    app.run(debug=True)
