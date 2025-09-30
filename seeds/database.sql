-- seeds_databases.sql

INSERT INTO "database" (name, description) VALUES
('postgresql', 'Base de datos relacional de código abierto, ideal para producción.'),
('mysql', 'Base de datos relacional ampliamente usada en aplicaciones web.'),
('sqlite', 'Base de datos ligera en un solo archivo, perfecta para desarrollo y pruebas.'),
('mongodb', 'Base de datos NoSQL orientada a documentos, muy usada en aplicaciones modernas.'),
('redis', 'Base de datos en memoria para caché y mensajería.'),
('oracle', 'Base de datos empresarial de alto rendimiento.'),
('mssql', 'Microsoft SQL Server, orientado a entornos corporativos.'),
('cassandra', 'Base de datos distribuida para grandes volúmenes de datos.'),
('dynamodb', 'Base de datos NoSQL de AWS totalmente gestionada.'),
('neo4j', 'Base de datos orientada a grafos, ideal para relaciones complejas.');
