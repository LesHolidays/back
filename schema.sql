CREATE TABLE Utilisateur (
  id_utilisateur INT PRIMARY KEY AUTO_INCREMENT, 
  nom VARCHAR(50) ,
  mdp VARCHAR(50) ,
  promo VARCHAR(5) ,
  points INT,
  actif BOOLEAN
)

CREATE TABLE Post (
  id_post INT PRIMARY KEY AUTO_INCREMENT , 
  images BLOB,
  description VARCHAR(50),
  date_post DATE
)

CREATE TABLE Vote (
  id_vote INT PRIMARY KEY AUTO_INCREMENT, 
  id_poste references ,
  id_utilisateur references ,
  date_vote DATE ,
  id_pour_qui_a_vote references
)

CREATE TABLE Commentaire(
  id_com INT PRIMARY KEY AUTO_INCREMENT, 
  id_utilisateur references ,
  id_post references ,
  date_commentaire DATE ,
  commentaire VARCHAR(255)
 )
