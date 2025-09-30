-- seeds_architecture_links.sql
-- Relaciona arquitecturas con bases de datos y tags
-- Tablas: architecturedatabaselink, architecturetaglink

-- 🔹 Arquitectura 1: fastapi-backend
INSERT INTO architecturedatabaselink (architecture_id, database_id)
SELECT a.id, d.id FROM architecture a, "database" d
WHERE a.name = 'fastapi-backend' AND d.name = 'postgresql'
ON CONFLICT DO NOTHING;

INSERT INTO architecturetaglink (architecture_id, tag_id)
SELECT a.id, t.id FROM architecture a, tag t
WHERE a.name = 'fastapi-backend' AND t.name IN ('fastapi','backend','api','docker')
ON CONFLICT DO NOTHING;

-- 🔹 Arquitectura 2: react-vite-frontend
INSERT INTO architecturetaglink (architecture_id, tag_id)
SELECT a.id, t.id FROM architecture a, tag t
WHERE a.name = 'react-vite-frontend' AND t.name IN ('react','frontend','typescript','vite')
ON CONFLICT DO NOTHING;

-- 🔹 Arquitectura 3: react-next-frontend
INSERT INTO architecturedatabaselink (architecture_id, database_id)
SELECT a.id, d.id FROM architecture a, "database" d
WHERE a.name = 'react-next-frontend' AND d.name = 'postgresql'
ON CONFLICT DO NOTHING;

INSERT INTO architecturetaglink (architecture_id, tag_id)
SELECT a.id, t.id FROM architecture a, tag t
WHERE a.name = 'react-next-frontend' AND t.name IN ('react','frontend','ssr','graphql')
ON CONFLICT DO NOTHING;

-- 🔹 Arquitectura 4: springboot-api
INSERT INTO architecturedatabaselink (architecture_id, database_id)
SELECT a.id, d.id FROM architecture a, "database" d
WHERE a.name = 'springboot-api' AND d.name = 'mysql'
ON CONFLICT DO NOTHING;

INSERT INTO architecturetaglink (architecture_id, tag_id)
SELECT a.id, t.id FROM architecture a, tag t
WHERE a.name = 'springboot-api' AND t.name IN ('spring-boot','backend','microservicios')
ON CONFLICT DO NOTHING;

-- 🔹 Arquitectura 5: fullstack-fastapi-react
INSERT INTO architecturedatabaselink (architecture_id, database_id)
SELECT a.id, d.id FROM architecture a, "database" d
WHERE a.name = 'fullstack-fastapi-react' AND d.name = 'postgresql'
ON CONFLICT DO NOTHING;

INSERT INTO architecturetaglink (architecture_id, tag_id)
SELECT a.id, t.id FROM architecture a, tag t
WHERE a.name = 'fullstack-fastapi-react' AND t.name IN ('fastapi','react','fullstack','postgresql')
ON CONFLICT DO NOTHING;

-- 🔹 Arquitectura 6: dashboard-analytics
INSERT INTO architecturedatabaselink (architecture_id, database_id)
SELECT a.id, d.id FROM architecture a, "database" d
WHERE a.name = 'dashboard-analytics' AND d.name IN ('postgresql','mongodb')
ON CONFLICT DO NOTHING;

INSERT INTO architecturetaglink (architecture_id, tag_id)
SELECT a.id, t.id FROM architecture a, tag t
WHERE a.name = 'dashboard-analytics' AND t.name IN ('analytics','dashboards','frontend')
ON CONFLICT DO NOTHING;

-- 🔹 Arquitectura 7: rag-chatbot
INSERT INTO architecturedatabaselink (architecture_id, database_id)
SELECT a.id, d.id FROM architecture a, "database" d
WHERE a.name = 'rag-chatbot' AND d.name = 'postgresql'
ON CONFLICT DO NOTHING;

INSERT INTO architecturetaglink (architecture_id, tag_id)
SELECT a.id, t.id FROM architecture a, tag t
WHERE a.name = 'rag-chatbot' AND t.name IN ('rag','chatbot','vector-db','nlp')
ON CONFLICT DO NOTHING;

-- 🔹 Arquitectura 8: ecommerce-next
INSERT INTO architecturedatabaselink (architecture_id, database_id)
SELECT a.id, d.id FROM architecture a, "database" d
WHERE a.name = 'ecommerce-next' AND d.name = 'mysql'
ON CONFLICT DO NOTHING;

INSERT INTO architecturetaglink (architecture_id, tag_id)
SELECT a.id, t.id FROM architecture a, tag t
WHERE a.name = 'ecommerce-next' AND t.name IN ('ecommerce','nextjs','frontend')
ON CONFLICT DO NOTHING;

-- 🔹 Arquitectura 9: saas-platform
INSERT INTO architecturedatabaselink (architecture_id, database_id)
SELECT a.id, d.id FROM architecture a, "database" d
WHERE a.name = 'saas-platform' AND d.name IN ('postgresql','mongodb')
ON CONFLICT DO NOTHING;

INSERT INTO architecturetaglink (architecture_id, tag_id)
SELECT a.id, t.id FROM architecture a, tag t
WHERE a.name = 'saas-platform' AND t.name IN ('saas','multi-tenant','scalability')
ON CONFLICT DO NOTHING;

-- 🔹 Arquitectura 10: microservices-springboot
INSERT INTO architecturedatabaselink (architecture_id, database_id)
SELECT a.id, d.id FROM architecture a, "database" d
WHERE a.name = 'microservices-springboot' AND d.name IN ('postgresql','mysql')
ON CONFLICT DO NOTHING;

INSERT INTO architecturetaglink (architecture_id, tag_id)
SELECT a.id, t.id FROM architecture a, tag t
WHERE a.name = 'microservices-springboot' AND t.name IN ('spring-boot','microservicios','docker','kubernetes')
ON CONFLICT DO NOTHING;
