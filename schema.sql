CREATE TABLE IF NOT EXISTS Utilisateur (
  id_utilisateur INTEGER PRIMARY KEY AUTOINCREMENT, 
  nom VARCHAR(50),
  prenom VARCHAR(50),
  mdp VARCHAR(50),
  promo VARCHAR(5),
  points INTEGER DEFAULT 0,
  actif BOOLEAN DEFAULT 0
);

CREATE TABLE IF NOT EXISTS Post (
  id_post INTEGER PRIMARY KEY AUTOINCREMENT, 
  image BLOB,
  description VARCHAR(50),
  date_post DATE
);

CREATE TABLE IF NOT EXISTS Vote (
  id_vote INTEGER PRIMARY KEY AUTOINCREMENT, 
  id_post INTEGER REFERENCES Post(id_post),
  id_utilisateur INTEGER REFERENCES Utilisateur(id_utilisateur),
  date_vote DATE,
  id_pour_qui_a_vote INTEGER REFERENCES Utilisateur(id_utilisateur)
);

CREATE TABLE IF NOT EXISTS Commentaire(
  id_com INTEGER PRIMARY KEY AUTOINCREMENT, 
  id_utilisateur INTEGER REFERENCES Utilisateur(id_utilisateur),
  id_post INTEGER REFERENCES Post(id_post),
  date_commentaire DATE,
  commentaire VARCHAR(255)

);

-- SELECT nom, prenom FROM utilisateur ORDER BY nom ASC

-- INSERT INTO utilisateur (compte) VALUES (?)

-- SELECT id_post FROM post
-- INSERT INTO post (vote) VALUES (?)
-- INSERT INTO post(commentaire) VALUES (?)
-- SELECT points FROM utilisateur
-- DELETE FROM post
-- UPDATE post SET description=?

-- INSERT INTO post (nouveau) VALUES (?)

-- SELECT points FROM utilisateur ORDER BY points DESC