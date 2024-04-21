-- Знайти які курси читає певний викладач. DONE
-- Це для всіх курсів
SELECT s.name AS subjectName, t.name as tutorName
FROM subjects as s
LEFT JOIN tutors as t ON s.tutor_id = t.id
WHERE t.id = 2
-- для передачі через консоль розкоментуйте наступний рядок, та закоментуйте попередній
-- WHERE t.id = ?
GROUP BY s.name ORDER BY tutorName ASC; 