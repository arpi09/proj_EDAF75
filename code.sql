-- Delete the tables if they exist.
-- Disable foreign key checks, so the tables can
-- be dropped in arbitrary order.
PRAGMA foreign_keys=OFF;

DROP TABLE IF EXISTS theater;
DROP TABLE IF EXISTS movie;
DROP TABLE IF EXISTS screening;
DROP TABLE IF EXISTS ticket;
DROP TABLE IF EXISTS customer;

PRAGMA foreign_keys=ON;



CREATE TABLE theater (
  name            TEXT,
  capacity        INT,
  PRIMARY KEY  (name)
);


CREATE TABLE movie (
  title           TEXT,
  prodYear        INT,
  IMDBKey         TEXT UNIQUE,
  PRIMARY KEY  (IMDBKey)
);

CREATE TABLE screening (
  performance_id  TEXT DEFAULT (lower(hex(randomblob(16)))),
  startTime       TIME,
  startDate       DATE,
  movie_IMDBKey   TEXT,
  theater_name      TEXT,
  PRIMARY KEY  (performance_id),
  FOREIGN KEY (movie_IMDBKey) REFERENCES  movie(IMDBKey),
  FOREIGN KEY (theater_name) REFERENCES  theater(name)
);


CREATE TABLE ticket (
  ti_id           TEXT DEFAULT (lower(hex(randomblob(16)))),
  customer_name     TEXT,
  performance_id    TEXT,
  PRIMARY KEY  (ti_id),
  FOREIGN KEY (performance_id)
  REFERENCES   screening(performance_id),
  FOREIGN KEY (customer_name) REFERENCES customer(userName)
);


CREATE TABLE customer (
  userName        TEXT UNIQUE,
  fullName        TEXT,
  password        TEXT,
  PRIMARY KEY  (userName)
);



-- Insert data into the tables.

INSERT INTO movie (title, prodYear, IMDBKey)
VALUES ('The Room', 2003, 'tt0368226');

INSERT INTO movie (title, prodYear, IMDBKey)
VALUES ('Troll 2', 1990, 'tt0105643');

INSERT INTO movie (title, prodYear, IMDBKey)
VALUES ('The incredible bulk', 2012, 'tt1788453');

INSERT INTO theater (name, capacity)
VALUES ('Filmstaden', 120);

INSERT INTO theater (name, capacity)
VALUES ('Kino', 100);

INSERT INTO screening (startTime,  startDate, movie_IMDBKey, theater_name)
  VALUES ('19:30', '2019–02-10', 'tt0368226','Kino');

INSERT INTO screening (startTime,  startDate, movie_IMDBKey, theater_name)
VALUES ('20:30', '2019–02-11', 'tt0105643','Filmstaden');

INSERT INTO screening (startTime,  startDate, movie_IMDBKey, theater_name)
VALUES ('19:00', '2019–02-12', 'tt1788453','Kino');

INSERT INTO customer (userName, fullName, password)
VALUES ('Eater1337', 'Hannibal Lecter', 'thisisnothashed');

INSERT INTO customer (userName, fullName, password)
VALUES ('Johnny', 'Jack Torrance', 'thisisnothashed');
