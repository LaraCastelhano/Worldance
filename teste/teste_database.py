from database import get_db

# sys.path.append(str(Path(__file__).resolve().parent.parent))


conn = get_db()

cursor = conn.cursor()

cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type = 'table';
""")

tabelas = cursor.fetchall()

print("Tabelas existentes na base de dados:")

for tabela in tabelas:
    print(tabela[0])

for tabela in ["aluno", "professores", "turma", "inscricao"]:

    cursor.execute(f"PRAGMA table_info({tabela});")

    colunas = cursor.fetchall()

    print(f"\nEstrutura da tabela {tabela}:")

    for coluna in colunas:
        print(coluna)

for tabela in ["turma", "inscricao"]:

    cursor.execute(f"PRAGMA foreign_key_list({tabela});")

    chaves = cursor.fetchall()

    print(f"\nRelações da tabela {tabela}:")

    for chave in chaves:
        print(chave)

cursor.execute("PRAGMA foreign_key_list(turma);")
print("\nChaves estrangeiras da tabela turma:")
print(cursor.fetchall())

conn.close()
