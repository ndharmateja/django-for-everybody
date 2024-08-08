CREATE TABLE Ages ( 
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
  name VARCHAR(128), 
  age INTEGER
);

DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Malakhy', 14);
INSERT INTO Ages (name, age) VALUES ('Tiree', 33);
INSERT INTO Ages (name, age) VALUES ('Lagan', 29);
INSERT INTO Ages (name, age) VALUES ('Eni', 39);
INSERT INTO Ages (name, age) VALUES ('Mehmet', 14);
INSERT INTO Ages (name, age) VALUES ('Windsor', 23);

SELECT hex(name || age) AS X FROM Ages ORDER BY X;