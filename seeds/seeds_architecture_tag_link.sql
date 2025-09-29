-- seeds_architecture_tag_link.sql

INSERT INTO architecture_tag_link (architecture_id, tag_id) VALUES
(1, (SELECT id FROM tag WHERE name = 'fastapi')),
(1, (SELECT id FROM tag WHERE name = 'backend')),
(1, (SELECT id FROM tag WHERE name = 'api')),
(1, (SELECT id FROM tag WHERE name = 'docker'));

INSERT INTO architecture_tag_link (architecture_id, tag_id) VALUES
(2, (SELECT id FROM tag WHERE name = 'react')),
(2, (SELECT id FROM tag WHERE name = 'frontend')),
(2, (SELECT id FROM tag WHERE name = 'typescript')),
(2, (SELECT id FROM tag WHERE name = 'vite'));

INSERT INTO architecture_tag_link (architecture_id, tag_id) VALUES
(3, (SELECT id FROM tag WHERE name = 'react')),
(3, (SELECT id FROM tag WHERE name = 'frontend')),
(3, (SELECT id FROM tag WHERE name = 'ssr')),
(3, (SELECT id FROM tag WHERE name = 'graphql'));

INSERT INTO architecture_tag_link (architecture_id, tag_id) VALUES
(4, (SELECT id FROM tag WHERE name = 'spring-boot')),
(4, (SELECT id FROM tag WHERE name = 'backend')),
(4, (SELECT id FROM tag WHERE name = 'microservicios'));

INSERT INTO architecture_tag_link (architecture_id, tag_id) VALUES
(5, (SELECT id FROM tag WHERE name = 'fastapi')),
(5, (SELECT id FROM tag WHERE name = 'react')),
(5, (SELECT id FROM tag WHERE name = 'fullstack')),
(5, (SELECT id FROM tag WHERE name = 'postgresql'));

INSERT INTO architecture_tag_link (architecture_id, tag_id) VALUES
(6, (SELECT id FROM tag WHERE name = 'analytics')),
(6, (SELECT id FROM tag WHERE name = 'dashboards')),
(6, (SELECT id FROM tag WHERE name = 'frontend'));

INSERT INTO architecture_tag_link (architecture_id, tag_id) VALUES
(7, (SELECT id FROM tag WHERE name = 'rag')),
(7, (SELECT id FROM tag WHERE name = 'chatbot')),
(7, (SELECT id FROM tag WHERE name = 'vector-db')),
(7, (SELECT id FROM tag WHERE name = 'nlp'));

INSERT INTO architecture_tag_link (architecture_id, tag_id) VALUES
(8, (SELECT id FROM tag WHERE name = 'ecommerce')),
(8, (SELECT id FROM tag WHERE name = 'nextjs')),
(8, (SELECT id FROM tag WHERE name = 'frontend'));

INSERT INTO architecture_tag_link (architecture_id, tag_id) VALUES
(9, (SELECT id FROM tag WHERE name = 'saas')),
(9, (SELECT id FROM tag WHERE name = 'multi-tenant')),
(9, (SELECT id FROM tag WHERE name = 'scalability'));

INSERT INTO architecture_tag_link (architecture_id, tag_id) VALUES
(10, (SELECT id FROM tag WHERE name = 'spring-boot')),
(10, (SELECT id FROM tag WHERE name = 'microservicios')),
(10, (SELECT id FROM tag WHERE name = 'docker')),
(10, (SELECT id FROM tag WHERE name = 'kubernetes'));
