from database import get_db

conn = get_db()
for tabela in ["aluno", "professores", "turma", "inscricao"]:
    n = conn.execute(f"SELECT COUNT(*) FROM {tabela}").fetchone()[0]
    print(tabela, n)
conn.close()
