import sqlite3
from database import get_db


def inserir_aluno(nome, email, telefone):
    conn = get_db()
    try:
        with conn:
            conn.execute(
                "INSERT INTO aluno (nome, email, telefone) VALUES (?, ?, ?)",
                (nome, email, telefone),
            )
    finally:
        conn.close()


def listar_alunos():
    conn = get_db()
    try:
        conn.row_factory = sqlite3.Row
        linhas = conn.execute(
            "SELECT id_aluno, nome, email, telefone "
            "FROM aluno ORDER BY nome COLLATE NOCASE, id_aluno"
        ).fetchall()
        return [dict(linha) for linha in linhas]
    finally:
        conn.close()
