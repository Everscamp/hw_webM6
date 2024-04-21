-- Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
SELECT ROUND(AVG(m.mark), 1) AS RoundedValue, s.name
FROM marks as m
LEFT JOIN students as s ON m.student_id = s.id
GROUP BY s.name ORDER BY
    RoundedValue DESC LIMIT 5;