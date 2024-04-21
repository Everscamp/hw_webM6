-- Список курсів, які певному студенту читає певний викладач.
SELECT sub.name AS Subject, t.name AS tutorName, s.name as Student
FROM subjects as sub
LEFT JOIN marks as m ON m.subject_id = sub.id
LEFT JOIN students as s ON m.student_id = s.id
LEFT JOIN tutors as t ON sub.tutor_id = t.id
WHERE s.id = 1 AND t.id = 5
-- для передачі через консоль розкоментуйте наступний рядок, та закоментуйте попередній
-- WHERE s.id = ? AND t.id = ?
GROUP BY Subject;