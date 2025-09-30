-- seeds_users.sql
INSERT INTO "user" (username, email, is_active, created_at) VALUES
('markus', 'markus@example.com', true, NOW()::text),
('lucia', 'lucia@example.com', true, NOW()::text),
('admin', 'admin@example.com', true, NOW()::text),
('guest', 'guest@example.com', false, NOW()::text),
('developer', 'dev@example.com', true, NOW()::text),
('designer', 'design@example.com', true, NOW()::text),
('tester', 'qa@example.com', true, NOW()::text),
('manager', 'manager@example.com', true, NOW()::text),
('student', 'student@example.com', true, NOW()::text),
('demo', 'demo@example.com', false, NOW()::text);
