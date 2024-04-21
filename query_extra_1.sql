-- Середній бал, який певний викладач ставить певному студентові.
SELECT ROUND(AVG(m.mark), 1) AS avMark, t.name AS Tutor, s.name as Student
FROM marks as m
LEFT JOIN subjects as sub ON m.subject_id = sub.id
LEFT JOIN students as s ON m.student_id = s.id
LEFT JOIN tutors as t ON sub.tutor_id = t.id
WHERE s.id = 2 AND t.id = 2;
-- для передачі через консоль розкоментуйте наступний рядок, та закоментуйте попередній
-- WHERE s.id = ? AND t.id = ?;