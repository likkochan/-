SELECT COUNT(*) FROM information_schema.tables (общее количество таблиц) 

SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES (все таблицы) 

SELECT * FROM users (пользователи) 

SELECT * FROM grades (оценки) 

SELECT * FROM users, grades WHERE users.user_id = grades.user_id (чьи оценки) 

SELECT * FROM users WHERE users.name = "Олег" (где олег)
