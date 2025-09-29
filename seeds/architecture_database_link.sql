-- seeds_architecture_database_link.sql

INSERT INTO architecture_database_link (architecture_id, database_id) VALUES
(1, (SELECT id FROM database WHERE name = 'postgresql'));

INSERT INTO architecture_database_link (architecture_id, database_id) VALUES
(3, (SELECT id FROM database WHERE name = 'postgresql'));

INSERT INTO architecture_database_link (architecture_id, database_id) VALUES
(4, (SELECT id FROM database WHERE name = 'mysql'));

INSERT INTO architecture_database_link (architecture_id, database_id) VALUES
(5, (SELECT id FROM database WHERE name = 'postgresql'));

INSERT INTO architecture_database_link (architecture_id, database_id) VALUES
(6, (SELECT id FROM database WHERE name = 'postgresql')),
(6, (SELECT id FROM database WHERE name = 'mongodb'));

INSERT INTO architecture_database_link (architecture_id, database_id) VALUES
(7, (SELECT id FROM database WHERE name = 'postgresql'));

INSERT INTO architecture_database_link (architecture_id, database_id) VALUES
(8, (SELECT id FROM database WHERE name = 'mysql'));

INSERT INTO architecture_database_link (architecture_id, database_id) VALUES
(9, (SELECT id FROM database WHERE name = 'postgresql')),
(9, (SELECT id FROM database WHERE name = 'mongodb'));

INSERT INTO architecture_database_link (architecture_id, database_id) VALUES
(10, (SELECT id FROM database WHERE name = 'postgresql')),
(10, (SELECT id FROM database WHERE name = 'mysql'));
