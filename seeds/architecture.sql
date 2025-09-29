-- seeds_architectures.sql

INSERT INTO architecture (name, type, description, path) VALUES
('fastapi-backend', 'fastapi', 'Arquitectura base para APIs con FastAPI.', '/templates/fastapi-backend'),
('react-vite-frontend', 'react_vite', 'Frontend moderno en React con Vite y TypeScript.', '/templates/react-vite-frontend'),
('react-next-frontend', 'react_next', 'Aplicación SSR/SSG con React y Next.js.', '/templates/react-next-frontend'),
('springboot-api', 'spring_boot', 'API backend usando Spring Boot.', '/templates/springboot-api'),
('fullstack-fastapi-react', 'fastapi', 'Stack completo: FastAPI + React Vite + PostgreSQL.', '/templates/fullstack-fastapi-react'),
('dashboard-analytics', 'react_vite', 'Dashboard con gráficas y analíticas.', '/templates/dashboard-analytics'),
('rag-chatbot', 'fastapi', 'Arquitectura de RAG: FastAPI backend + FAISS + modelo local.', '/templates/rag-chatbot'),
('ecommerce-next', 'react_next', 'Plantilla ecommerce con Next.js + integración de pagos.', '/templates/ecommerce-next'),
('saas-platform', 'fastapi', 'Arquitectura SaaS multi-tenant con FastAPI.', '/templates/saas-platform'),
('microservices-springboot', 'spring_boot', 'Arquitectura de microservicios basada en Spring Boot.', '/templates/microservices-springboot');
