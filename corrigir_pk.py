from database import get_db

conn = get_db()
conn.executescript("""
DROP TABLE IF EXISTS inscricao;
DROP TABLE IF EXISTS turma;

CREATE TABLE turma (
    id_turma INTEGER PRIMARY KEY AUTOINCREMENT,
    designacao TEXT,
    nivel_turma VARCHAR(50),
    horario TEXT,
    capacidade INTEGER,
    id_professor INTEGER NOT NULL,
    FOREIGN KEY (id_professor) REFERENCES professores (id_professor)
);

CREATE TABLE inscricao (
    id_inscricao INTEGER PRIMARY KEY AUTOINCREMENT,
    data_inscricao DATE,
    estado_inscricao VARCHAR(20),
    id_aluno INTEGER NOT NULL,
    id_turma INTEGER NOT NULL,
    FOREIGN KEY (id_aluno) REFERENCES aluno (id_aluno),
    FOREIGN KEY (id_turma) REFERENCES turma (id_turma)
);
""")
conn.close()
