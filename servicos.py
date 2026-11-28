from datetime import date
from persistencia import inserir_aluno, listar_alunos as _listar


def registar_aluno(nome, email, telefone, data_nascimento):
    nome = " ".join((nome or "").split())
    email = (email or "").strip()
    telefone = (telefone or "").strip()
    data_nascimento = (data_nascimento or "").strip()

    erros = []

    if not nome:
        erros.append(
            "O nome é obrigatório e não pode ficar vazio ou só com espaços.")
    elif len(nome) > 100:
        erros.append("O nome não pode ter mais de 100 caracteres.")

    if not email:
        erros.append("O email é obrigatório.")
    else:
        partes = email.split("@")
        if len(partes) != 2 or not partes[0] or "." not in partes[1]:
            erros.append("O email não é válido.")

    if len(telefone) > 15:
        erros.append("O telefone não pode ter mais de 15 caracteres.")

    data_iso = None
    if not data_nascimento:
        erros.append("A data de nascimento é obrigarória.")
    else:
        try:
            nascimento = date.fromisoformat(data_nascimento)
        except ValueError:
            erros.append("A data de nascimento não é válida.")
        else:
            if nascimento > date.today():
                erros.append("A data de nascimento não é válida.")
            elif nascimento.year < 1900:
                erros.append("A data de nascimento não é válida.")
            else:
                data_iso = nascimento.isoformat()

    if erros:
        return False, erros

    inserir_aluno(nome, email, telefone or None, data_iso)
    return True, []


def listar_alunos():
    alunos = _listar()
    for aluno in alunos:
        texto = aluno["data_nascimento"]
        if texto:
            try:
                aluno["data_nascimento"] = date.fromisoformat(
                    texto).strftime("%d/%m/%Y")
            except ValueError:
                pass
    return alunos
