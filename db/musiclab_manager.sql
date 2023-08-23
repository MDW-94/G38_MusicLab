DROP TABLE IF EXISTS artists;
DROP TABLE IF EXISTS albums;


CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR (255),
    genre VARCHAR (255),
    artist_id INT NOT NULL REFERENCES artists(id),
    tracklist INT
);


INSERT INTO artists (name) VALUES('The Beatles');
INSERT INTO artists (name) VALUES('Elvis Presley');
INSERT INTO artists (name) VALUES('Michael Jackson');

-- INSERT INTO albums (title, genre, artist_id, tracklist) VALUES ('Sgt Peppers Lonely Hearts Club Band', 'Rock', artist, 10)
-- INSERT INTO albums (title, genre, artist_id, tracklist) VALUES ('How Great Thou Art', 'Gospel', artist, 13)
-- INSERT INTO albums (title, genre, artist_id, tracklist) VALUES ('Thriller', 'Pop', artist, 15)


