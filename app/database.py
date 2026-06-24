import sqlite3
import os

DATABASE = os.environ.get('DATABASE_PATH', 'database.db')

def init_db():
    conn = sqlite3.connect(DATABASE)

    with open('schema.sql') as f:
        conn.executescript(f.read())

    cur = conn.cursor()

    try:
        cur.execute("INSERT INTO User (user_id, last_name, first_name, year) VALUES (?, ?, ?, ?)",
                    (1, 'Albert', 'Corentin', 'IMAC1')
                    )

        cur.execute("INSERT INTO User (user_id, last_name, first_name, year) VALUES (?, ?, ?, ?)",
                    (2, 'Azizi', 'Romana', 'IMAC1')
                    )

        cur.execute("INSERT INTO User (user_id, last_name, first_name, year) VALUES (?, ?, ?, ?)",
                    (3, 'Baraille', 'Benoît', 'IMAC1')
                    )

        cur.execute("INSERT INTO User (user_id, last_name, first_name, year) VALUES (?, ?, ?, ?)",
                    (4, 'Bleuze', 'Lucille', 'IMAC1')
                    )

        cur.execute("INSERT INTO User (user_id, last_name, first_name, year) VALUES (?, ?, ?, ?)",
                    (5, 'Boire', 'Yasmine', 'IMAC1')
                    )

        cur.execute("INSERT INTO User (user_id, last_name, first_name, year) VALUES (?, ?, ?, ?)",
                    (6, 'Bonne', 'Julie', 'IMAC1')
                    )

        cur.execute("INSERT INTO User (user_id, last_name, first_name, year) VALUES (?, ?, ?, ?)",
                    (7, 'Bonnet', 'Alexandre', 'IMAC1')
                    )

        cur.execute("INSERT INTO User (user_id, last_name, first_name, year) VALUES (?, ?, ?, ?)",
                    (8, 'Bredeau', 'Kellian', 'IMAC1')
                    )

        cur.execute("INSERT INTO User (user_id, last_name, first_name, year) VALUES (?, ?, ?, ?)",
                    (9, 'Cadete', 'Raphael', 'IMAC1')
                    )

        cur.execute("INSERT INTO User (user_id, last_name, first_name, year) VALUES (?, ?, ?, ?)",
                    (10, 'Chabaud', 'Chloé', 'IMAC1')
                    )

        cur.execute("INSERT INTO User (user_id, last_name, first_name, year) VALUES (?, ?, ?, ?)",
                    (11, 'Duperrier', 'Mila', 'IMAC1')
                    )

        cur.execute("INSERT INTO User (user_id, last_name, first_name, year) VALUES (?, ?, ?, ?)",
                    (12, 'Farandjis', 'Matthieu', 'IMAC1')
                    )

        cur.execute("INSERT INTO User (user_id, last_name, first_name, year) VALUES (?, ?, ?, ?)",
                    (13, 'Fournier', 'Léna', 'IMAC1')
                    )

        cur.execute("INSERT INTO User (user_id, last_name, first_name, year) VALUES (?, ?, ?, ?)",
                    (14, 'Grosdidier', 'Alexandre', 'IMAC1')
                    )

        cur.execute("INSERT INTO User (user_id, last_name, first_name, year) VALUES (?, ?, ?, ?)",
                    (15, 'Jacquemin', 'Roméo', 'IMAC1')
                    )

        cur.execute("INSERT INTO User (user_id, last_name, first_name, year) VALUES (?, ?, ?, ?)",
                    (16, 'Jouvet', 'Romane', 'IMAC1')
                    )

        cur.execute("INSERT INTO User (user_id, last_name, first_name, year) VALUES (?, ?, ?, ?)",
                    (17, 'Kowalik', 'Laïn', 'IMAC1')
                    )

        cur.execute("INSERT INTO User (user_id, last_name, first_name, year) VALUES (?, ?, ?, ?)",
                    (18, 'Larabi', 'Lalie', 'IMAC1')
                    )

        cur.execute("INSERT INTO User (user_id, last_name, first_name, year) VALUES (?, ?, ?, ?)",
                    (19, 'Le Poulain', 'Elouan', 'IMAC1')
                    )

        cur.execute("INSERT INTO User (user_id, last_name, first_name, year) VALUES (?, ?, ?, ?)",
                    (20, 'Leeder', 'Julien', 'IMAC1')
                    )

        cur.execute("INSERT INTO User (user_id, last_name, first_name, year) VALUES (?, ?, ?, ?)",
                    (21, 'Marteau--Bazouni', 'Romane', 'IMAC1')
                    )

        cur.execute("INSERT INTO User (user_id, last_name, first_name, year) VALUES (?, ?, ?, ?)",
                    (22, 'Moreau--Thomas', 'Nils', 'IMAC1')
                    )

        cur.execute("INSERT INTO User (user_id, last_name, first_name, year) VALUES (?, ?, ?, ?)",
                    (23, 'Olivier', 'Agathe', 'IMAC1')
                    )

        cur.execute("INSERT INTO User (user_id, last_name, first_name, year) VALUES (?, ?, ?, ?)",
                    (24, 'Phetdara', 'Souksana', 'IMAC1')
                    )

        cur.execute("INSERT INTO User (user_id, last_name, first_name, year) VALUES (?, ?, ?, ?)",
                    (25, 'Poirot', 'Éléa', 'IMAC1')
                    )

        cur.execute("INSERT INTO User (user_id, last_name, first_name, year) VALUES (?, ?, ?, ?)",
                    (26, 'Riesen', 'Jade', 'IMAC1')
                    )

        cur.execute("INSERT INTO User (user_id, last_name, first_name, year) VALUES (?, ?, ?, ?)",
                    (27, 'Slimane', 'Marine', 'IMAC1')
                    )

        cur.execute("INSERT INTO User (user_id, last_name, first_name, year) VALUES (?, ?, ?, ?)",
                    (28, 'Varo Tupin', 'Romane', 'IMAC1')
                    )

        cur.execute("INSERT INTO User (user_id, last_name, first_name, year) VALUES (?, ?, ?, ?)",
                    (29, 'Verger', 'Justine', 'IMAC1')
                    )

        cur.execute("INSERT INTO User (user_id, last_name, first_name, year) VALUES (?, ?, ?, ?)",
                    (30, 'Wong', 'Yanis', 'IMAC1')
                    )

        cur.execute("INSERT INTO User (user_id, last_name, first_name, year) VALUES (?, ?, ?, ?)",
                    (31, 'Zhyla', 'Alina', 'IMAC1')
                    )
        conn.commit()
    except:
        pass
    finally:
        conn.close()

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        value = row[idx]
        if isinstance(value, bytes):
            try:
                value = value.decode('utf-8')
            except UnicodeDecodeError:
                value = str(value)
                
        d[col[0]] = value
    return d

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = dict_factory
    return conn