from flask import Flask, render_template, request, redirect, url_for, flash

from database import init_db
import servicos

app = Flask(__name__)
app.secret_key = "chave-de-desenvolvimento"

init_db()


@app.route("/")
def pagina_inicial():
    return redirect(url_for("listar_alunos"))


@app.route("/alunos")
def listar_alunos():
    alunos = servicos.listar_alunos()
    return render_template("alunos.html", alunos=alunos)


@app.route("/alunos/novo", methods=["GET", "POST"])
def novo_aluno():
    if request.method == "GET":
        return render_template("aluno_form.html", erros=[], dados={})

    dados = {
        "nome": request.form.get("nome", ""),
        "email": request.form.get("email", ""),
        "telefone": request.form.get("telefone", ""),
    }
    ok, erros = servicos.registar_aluno(**dados)

    if not ok:
        return render_template("aluno_form.html", erros=erros, dados=dados), 422

    flash("Aluno registado com sucesso!")
    return redirect(url_for("listar_alunos"))


if __name__ == "__main__":
    app.run(debug=True)
