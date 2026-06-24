CREATE TABLE IF NOT EXISTS User (
  user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
  last_name VARCHAR(50),
  first_name VARCHAR(50),
  password VARCHAR(100),
  year VARCHAR(5),
  points INTEGER DEFAULT 0,
  activated BOOLEAN DEFAULT 0
);

CREATE TABLE IF NOT EXISTS Post (
  post_id INTEGER PRIMARY KEY AUTOINCREMENT, 
  user_id INTEGER REFERENCES User(user_id),
  image BLOB,
  description VARCHAR(50),
  creation_date DATE
);

CREATE TABLE IF NOT EXISTS Vote (
  post_id INTEGER REFERENCES Post(post_id),
  user_id INTEGER REFERENCES User(user_id),
  vote_date DATE,
  voted_user_id INTEGER REFERENCES User(user_id),

  PRIMARY KEY (user_id, post_id, voted_user_id)
);

CREATE TABLE IF NOT EXISTS Commentary(
  commentary_id INTEGER PRIMARY KEY AUTOINCREMENT, 
  user_id INTEGER REFERENCES User(user_id),
  post_id INTEGER REFERENCES Post(post_id),
  creation_date DATE,
  message VARCHAR(255)

);

-- SELECT nom, prenom FROM utilisateur ORDER BY nom ASC

-- INSERT INTO utilisateur (compte) VALUES (?)

-- SELECT post_id FROM post
-- INSERT INTO post (vote) VALUES (?)
-- INSERT INTO post(commentaire) VALUES (?)
-- SELECT points FROM utilisateur
-- DELETE FROM post
-- UPDATE post SET description=?

-- INSERT INTO post (nouveau) VALUES (?)

-- SELECT points FROM utilisateur ORDER BY points DESC