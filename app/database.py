import sqlite3

DATABASE = 'database.db'

def init_db():
    conn = sqlite3.connect(DATABASE)

    with open('schema.sql') as f:
        conn.executescript(f.read())

    cur = conn.cursor()

    cur.execute("INSERT INTO Utilisateur (nom, prenom, promo) VALUES (?, ?, ?)",
                ('Albert', 'Corentin', 'IMAC1')
                )

    cur.execute("INSERT INTO Utilisateur (nom, prenom, promo) VALUES (?, ?, ?)",
                ('Azizi', 'Romana', 'IMAC1')
                )

    cur.execute("INSERT INTO Utilisateur (nom, prenom, promo) VALUES (?, ?, ?)",
                ('Baraille', 'Benoît', 'IMAC1')
                )

    cur.execute("INSERT INTO Utilisateur (nom, prenom, promo) VALUES (?, ?, ?)",
                ('Bleuze', 'Lucille', 'IMAC1')
                )

    cur.execute("INSERT INTO Utilisateur (nom, prenom, promo) VALUES (?, ?, ?)",
                ('Boire', 'Yasmine', 'IMAC1')
                )

    cur.execute("INSERT INTO Utilisateur (nom, prenom, promo) VALUES (?, ?, ?)",
                ('Bonne', 'Julie', 'IMAC1')
                )

    cur.execute("INSERT INTO Utilisateur (nom, prenom, promo) VALUES (?, ?, ?)",
                ('Bonnet', 'Alexandre', 'IMAC1')
                )

    cur.execute("INSERT INTO Utilisateur (nom, prenom, promo) VALUES (?, ?, ?)",
                ('Bredeau', 'Kellian', 'IMAC1')
                )

    cur.execute("INSERT INTO Utilisateur (nom, prenom, promo) VALUES (?, ?, ?)",
                ('Cadete', 'Raphael', 'IMAC1')
                )

    cur.execute("INSERT INTO Utilisateur (nom, prenom, promo) VALUES (?, ?, ?)",
                ('Chabaud', 'Chloé', 'IMAC1')
                )

    cur.execute("INSERT INTO Utilisateur (nom, prenom, promo) VALUES (?, ?, ?)",
                ('Duperrier', 'Mila', 'IMAC1')
                )

    cur.execute("INSERT INTO Utilisateur (nom, prenom, promo) VALUES (?, ?, ?)",
                ('Farandjis', 'Matthieu', 'IMAC1')
                )

    cur.execute("INSERT INTO Utilisateur (nom, prenom, promo) VALUES (?, ?, ?)",
                ('Fournier', 'Léna', 'IMAC1')
                )

    cur.execute("INSERT INTO Utilisateur (nom, prenom, promo) VALUES (?, ?, ?)",
                ('Grosdidier', 'Alexandre', 'IMAC1')
                )

    cur.execute("INSERT INTO Utilisateur (nom, prenom, promo) VALUES (?, ?, ?)",
                ('Jacquemin', 'Roméo', 'IMAC1')
                )

    cur.execute("INSERT INTO Utilisateur (nom, prenom, promo) VALUES (?, ?, ?)",
                ('Jouvet', 'Romane', 'IMAC1')
                )

    cur.execute("INSERT INTO Utilisateur (nom, prenom, promo) VALUES (?, ?, ?)",
                ('Kowalik', 'Laïn', 'IMAC1')
                )

    cur.execute("INSERT INTO Utilisateur (nom, prenom, promo) VALUES (?, ?, ?)",
                ('Larabi', 'Lalie', 'IMAC1')
                )

    cur.execute("INSERT INTO Utilisateur (nom, prenom, promo) VALUES (?, ?, ?)",
                ('Le Poulain', 'Elouan', 'IMAC1')
                )

    cur.execute("INSERT INTO Utilisateur (nom, prenom, promo) VALUES (?, ?, ?)",
                ('Leeder', 'Julien', 'IMAC1')
                )

    cur.execute("INSERT INTO Utilisateur (nom, prenom, promo) VALUES (?, ?, ?)",
                ('Marteau--Bazouni', 'Romane', 'IMAC1')
                )

    cur.execute("INSERT INTO Utilisateur (nom, prenom, promo) VALUES (?, ?, ?)",
                ('Moreau--Thomas', 'Nils', 'IMAC1')
                )

    cur.execute("INSERT INTO Utilisateur (nom, prenom, promo) VALUES (?, ?, ?)",
                ('Olivier', 'Agathe', 'IMAC1')
                )

    cur.execute("INSERT INTO Utilisateur (nom, prenom, promo) VALUES (?, ?, ?)",
                ('Phetdara', 'Souksana', 'IMAC1')
                )

    cur.execute("INSERT INTO Utilisateur (nom, prenom, promo) VALUES (?, ?, ?)",
                ('Poirot', 'Éléa', 'IMAC1')
                )

    cur.execute("INSERT INTO Utilisateur (nom, prenom, promo) VALUES (?, ?, ?)",
                ('Riesen', 'Jade', 'IMAC1')
                )

    cur.execute("INSERT INTO Utilisateur (nom, prenom, promo) VALUES (?, ?, ?)",
                ('Slimane', 'Marine', 'IMAC1')
                )

    cur.execute("INSERT INTO Utilisateur (nom, prenom, promo) VALUES (?, ?, ?)",
                ('Varo Tupin', 'Romane', 'IMAC1')
                )

    cur.execute("INSERT INTO Utilisateur (nom, prenom, promo) VALUES (?, ?, ?)",
                ('Verger', 'Justine', 'IMAC1')
                )

    cur.execute("INSERT INTO Utilisateur (nom, prenom, promo) VALUES (?, ?, ?)",
                ('Wong', 'Yanis', 'IMAC1')
                )

    cur.execute("INSERT INTO Utilisateur (nom, prenom, promo) VALUES (?, ?, ?)",
                ('Zhyla', 'Alina', 'IMAC1')
                )

    conn.commit()
    conn.close()

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn