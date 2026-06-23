import sqlite3

DATABASE = 'database.db'

def init_db():
    conn = sqlite3.connect(DATABASE)

    with open('schema.sql') as f:
        conn.executescript(f.read())

    cur = conn.cursor()

    cur.execute("INSERT INTO Utilisateur (nom, promo) VALUES (?, ?)",
                ('Mila', 'IMAC1')
                )

    cur.execute("INSERT INTO Utilisateur (nom, promo) VALUES (?, ?)",
                ('Yasmine', 'IMAC1')
                )

    cur.execute("INSERT INTO Utilisateur (nom, promo) VALUES (?, ?)",
                ('Corentin', 'IMAC1')
                )

    conn.commit()
    conn.close()

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn