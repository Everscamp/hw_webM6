-- Знайти середній бал на потоці (по всій таблиці оцінок). DONE
SELECT ROUND(AVG(m.mark), 1) AS RoundedValue
FROM marks as m; 