import sqlite3

DATABASE = 'database.db'

def init_db():
    conn = sqlite3.connect(DATABASE)

    with open('schema.sql') as f:
        conn.executescript(f.read())

    cur = conn.cursor()

    try:
        cur.execute("INSERT INTO Utilisateur (id_utilisateur, nom, prenom, promo) VALUES (?, ?, ?, ?)",
                    (1, 'Albert', 'Corentin', 'IMAC1')
                    )

        cur.execute("INSERT INTO Utilisateur (id_utilisateur, nom, prenom, promo) VALUES (?, ?, ?, ?)",
                    (2, 'Azizi', 'Romana', 'IMAC1')
                    )

        cur.execute("INSERT INTO Utilisateur (id_utilisateur, nom, prenom, promo) VALUES (?, ?, ?, ?)",
                    (3, 'Baraille', 'Benoît', 'IMAC1')
                    )

        cur.execute("INSERT INTO Utilisateur (id_utilisateur, nom, prenom, promo) VALUES (?, ?, ?, ?)",
                    (4, 'Bleuze', 'Lucille', 'IMAC1')
                    )

        cur.execute("INSERT INTO Utilisateur (id_utilisateur, nom, prenom, promo) VALUES (?, ?, ?, ?)",
                    (5, 'Boire', 'Yasmine', 'IMAC1')
                    )

        cur.execute("INSERT INTO Utilisateur (id_utilisateur, nom, prenom, promo) VALUES (?, ?, ?, ?)",
                    (6, 'Bonne', 'Julie', 'IMAC1')
                    )

        cur.execute("INSERT INTO Utilisateur (id_utilisateur, nom, prenom, promo) VALUES (?, ?, ?, ?)",
                    (7, 'Bonnet', 'Alexandre', 'IMAC1')
                    )

        cur.execute("INSERT INTO Utilisateur (id_utilisateur, nom, prenom, promo) VALUES (?, ?, ?, ?)",
                    (8, 'Bredeau', 'Kellian', 'IMAC1')
                    )

        cur.execute("INSERT INTO Utilisateur (id_utilisateur, nom, prenom, promo) VALUES (?, ?, ?, ?)",
                    (9, 'Cadete', 'Raphael', 'IMAC1')
                    )

        cur.execute("INSERT INTO Utilisateur (id_utilisateur, nom, prenom, promo) VALUES (?, ?, ?, ?)",
                    (10, 'Chabaud', 'Chloé', 'IMAC1')
                    )

        cur.execute("INSERT INTO Utilisateur (id_utilisateur, nom, prenom, promo) VALUES (?, ?, ?, ?)",
                    (11, 'Duperrier', 'Mila', 'IMAC1')
                    )

        cur.execute("INSERT INTO Utilisateur (id_utilisateur, nom, prenom, promo) VALUES (?, ?, ?, ?)",
                    (12, 'Farandjis', 'Matthieu', 'IMAC1')
                    )

        cur.execute("INSERT INTO Utilisateur (id_utilisateur, nom, prenom, promo) VALUES (?, ?, ?, ?)",
                    (13, 'Fournier', 'Léna', 'IMAC1')
                    )

        cur.execute("INSERT INTO Utilisateur (id_utilisateur, nom, prenom, promo) VALUES (?, ?, ?, ?)",
                    (14, 'Grosdidier', 'Alexandre', 'IMAC1')
                    )

        cur.execute("INSERT INTO Utilisateur (id_utilisateur, nom, prenom, promo) VALUES (?, ?, ?, ?)",
                    (15, 'Jacquemin', 'Roméo', 'IMAC1')
                    )

        cur.execute("INSERT INTO Utilisateur (id_utilisateur, nom, prenom, promo) VALUES (?, ?, ?, ?)",
                    (16, 'Jouvet', 'Romane', 'IMAC1')
                    )

        cur.execute("INSERT INTO Utilisateur (id_utilisateur, nom, prenom, promo) VALUES (?, ?, ?, ?)",
                    (17, 'Kowalik', 'Laïn', 'IMAC1')
                    )

        cur.execute("INSERT INTO Utilisateur (id_utilisateur, nom, prenom, promo) VALUES (?, ?, ?, ?)",
                    (18, 'Larabi', 'Lalie', 'IMAC1')
                    )

        cur.execute("INSERT INTO Utilisateur (id_utilisateur, nom, prenom, promo) VALUES (?, ?, ?, ?)",
                    (19, 'Le Poulain', 'Elouan', 'IMAC1')
                    )

        cur.execute("INSERT INTO Utilisateur (id_utilisateur, nom, prenom, promo) VALUES (?, ?, ?, ?)",
                    (20, 'Leeder', 'Julien', 'IMAC1')
                    )

        cur.execute("INSERT INTO Utilisateur (id_utilisateur, nom, prenom, promo) VALUES (?, ?, ?, ?)",
                    (21, 'Marteau--Bazouni', 'Romane', 'IMAC1')
                    )

        cur.execute("INSERT INTO Utilisateur (id_utilisateur, nom, prenom, promo) VALUES (?, ?, ?, ?)",
                    (22, 'Moreau--Thomas', 'Nils', 'IMAC1')
                    )

        cur.execute("INSERT INTO Utilisateur (id_utilisateur, nom, prenom, promo) VALUES (?, ?, ?, ?)",
                    (23, 'Olivier', 'Agathe', 'IMAC1')
                    )

        cur.execute("INSERT INTO Utilisateur (id_utilisateur, nom, prenom, promo) VALUES (?, ?, ?, ?)",
                    (24, 'Phetdara', 'Souksana', 'IMAC1')
                    )

        cur.execute("INSERT INTO Utilisateur (id_utilisateur, nom, prenom, promo) VALUES (?, ?, ?, ?)",
                    (25, 'Poirot', 'Éléa', 'IMAC1')
                    )

        cur.execute("INSERT INTO Utilisateur (id_utilisateur, nom, prenom, promo) VALUES (?, ?, ?, ?)",
                    (26, 'Riesen', 'Jade', 'IMAC1')
                    )

        cur.execute("INSERT INTO Utilisateur (id_utilisateur, nom, prenom, promo) VALUES (?, ?, ?, ?)",
                    (27, 'Slimane', 'Marine', 'IMAC1')
                    )

        cur.execute("INSERT INTO Utilisateur (id_utilisateur, nom, prenom, promo) VALUES (?, ?, ?, ?)",
                    (28, 'Varo Tupin', 'Romane', 'IMAC1')
                    )

        cur.execute("INSERT INTO Utilisateur (id_utilisateur, nom, prenom, promo) VALUES (?, ?, ?, ?)",
                    (29, 'Verger', 'Justine', 'IMAC1')
                    )

        cur.execute("INSERT INTO Utilisateur (id_utilisateur, nom, prenom, promo) VALUES (?, ?, ?, ?)",
                    (30, 'Wong', 'Yanis', 'IMAC1')
                    )

        cur.execute("INSERT INTO Utilisateur (id_utilisateur, nom, prenom, promo) VALUES (?, ?, ?, ?)",
                    (31, 'Zhyla', 'Alina', 'IMAC1')
                    )
        conn.commit()
    except:
        pass
    finally:
        conn.close()

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn