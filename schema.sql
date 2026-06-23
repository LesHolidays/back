CREATE TABLE Utilisateur (
  id_utilisateur INT PRIMARY KEY AUTO_INCREMENT, 
  nom VARCHAR(50),
  mdp VARCHAR(50),
  promo VARCHAR(5),
  points INT DEFAULT 0,
  actif BOOLEAN DEFAULT 0
)

CREATE TABLE Post (
  id_post INT PRIMARY KEY AUTO_INCREMENT, 
  images BLOB,
  description VARCHAR(50),
  date_post DATE DEFAULT CURRENT_DATE()
)

CREATE TABLE Vote (
  id_vote INT PRIMARY KEY AUTO_INCREMENT, 
  id_post REFERENCES Post(id),
  id_utilisateur REFERENCES Utilisateur(id),
  date_vote DATE DEFAULT CURRENT_DATE(),
  id_pour_qui_a_vote REFERENCES Utilisateur(id)
)

CREATE TABLE Commentaire(
  id_com INT PRIMARY KEY AUTO_INCREMENT, 
  id_utilisateur REFERENCES Utilisateur(id),
  id_post REFERENCES Post(id),
  date_commentaire DATE DEFAULT CURRENT_DATE(),
  commentaire VARCHAR(255)
)
