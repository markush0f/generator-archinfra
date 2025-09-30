-- seeds_projects.sql
-- Inserta proyectos con sus relaciones

-- Proyectos base
INSERT INTO project (name, description, created_at, updated_at, architecture_id) VALUES
('RAG Assistant', 'Asistente con RAG usando FastAPI + FAISS.', NOW(), NOW(), 7),
('Task Manager', 'Gestor de tareas con IA para priorización.', NOW(), NOW(), 5),
('Fitness Tracker', 'App para seguimiento de entrenamientos y nutrición.', NOW(), NOW(), 2),
('Music Generator', 'Generador de beats musicales con IA.', NOW(), NOW(), 1),
('Ecommerce Next', 'Tienda online con Next.js y pagos integrados.', NOW(), NOW(), 8),
('Analytics Dashboard', 'Dashboard para métricas de negocio.', NOW(), NOW(), 6),
('Tutor Online', 'Plataforma de tutorías con IA.', NOW(), NOW(), 3),
('Fintech Wallet', 'Billetera digital con análisis de gastos.', NOW(), NOW(), 9),
('Startup Lab', 'Plataforma para validar ideas de negocio.', NOW(), NOW(), 1),
('PetCare', 'App para seguimiento de mascotas y recordatorios médicos.', NOW(), NOW(), 2);

-- Relaciones con bases de datos (project_database_link)
INSERT INTO project_database_link (project_id, database_id) VALUES
(1, (SELECT id FROM database WHERE name = 'postgresql')),
(2, (SELECT id FROM database WHERE name = 'postgresql')),
(3, (SELECT id FROM database WHERE name = 'sqlite')),
(4, (SELECT id FROM database WHERE name = 'postgresql')),
(5, (SELECT id FROM database WHERE name = 'mysql')),
(6, (SELECT id FROM database WHERE name = 'postgresql')),
(6, (SELECT id FROM database WHERE name = 'mongodb')),
(7, (SELECT id FROM database WHERE name = 'postgresql')),
(8, (SELECT id FROM database WHERE name = 'postgresql')),
(9, (SELECT id FROM database WHERE name = 'mysql')),
(10, (SELECT id FROM database WHERE name = 'sqlite'));

-- Relaciones con tags (project_tag_link)
INSERT INTO project_tag_link (project_id, tag_id) VALUES
(1, (SELECT id FROM tag WHERE name = 'rag')),
(1, (SELECT id FROM tag WHERE name = 'chatbot')),
(1, (SELECT id FROM tag WHERE name = 'vector-db')),
(2, (SELECT id FROM tag WHERE name = 'productividad')),
(2, (SELECT id FROM tag WHERE name = 'gestor-proyectos')),
(3, (SELECT id FROM tag WHERE name = 'fitness')),
(3, (SELECT id FROM tag WHERE name = 'salud')),
(4, (SELECT id FROM tag WHERE name = 'musicgen')),
(4, (SELECT id FROM tag WHERE name = 'ia')),
(5, (SELECT id FROM tag WHERE name = 'ecommerce')),
(5, (SELECT id FROM tag WHERE name = 'frontend')),
(6, (SELECT id FROM tag WHERE name = 'analytics')),
(6, (SELECT id FROM tag WHERE name = 'dashboards')),
(7, (SELECT id FROM tag WHERE name = 'educacion')),
(7, (SELECT id FROM tag WHERE name = 'tutor')),
(8, (SELECT id FROM tag WHERE name = 'fintech')),
(8, (SELECT id FROM tag WHERE name = 'wallet')),
(9, (SELECT id FROM tag WHERE name = 'startup')),
(9, (SELECT id FROM tag WHERE name = 'mvp')),
(10, (SELECT id FROM tag WHERE name = 'mascotas')),
(10, (SELECT id FROM tag WHERE name = 'salud'));
