import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SQL_FILE = ROOT / 'Hello-World.db.sql'
DB_FILE = ROOT / 'Hello-World.db'

def init_db():
    if not SQL_FILE.exists():
        print('Arquivo Hello-World.db.sql não encontrado.')
        return
    sql = SQL_FILE.read_text()
    conn = sqlite3.connect(str(DB_FILE))
    cur = conn.cursor()
    cur.executescript(sql)
    conn.commit()
    conn.close()
    print('Banco inicializado em', DB_FILE)

if __name__ == '__main__':
    init_db()