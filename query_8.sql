-- Знайти середній бал, який ставить певний викладач зі своїх предметів.
SELECT ROUND(AVG(m.mark), 2) AS markValue, sub.name AS Subject, t.name AS tutorName
FROM marks as m
INNER JOIN subjects as sub ON m.subject_id = sub.id
LEFT JOIN tutors as t ON sub.tutor_id = t.id
WHERE t.id = 4
-- для передачі через консоль розкоментуйте наступний рядок, та закоментуйте попередній
-- WHERE t.id = ?
GROUP BY Subject; 