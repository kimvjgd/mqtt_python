-- SQLite
CREATE TABLE SENSORS(
  ID        INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  USER      CHAR(20),
  PLACE     CHAR(20),
  SENSOR    CHAR(20),
  VALUE     REAL,
  REG_DATE  DATETIME DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE SENSORS;