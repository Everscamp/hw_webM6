-- Знайти список курсів, які відвідує студент.
SELECT sub.name AS subjectName, s.name as studentName
FROM subjects as sub
LEFT JOIN marks as m ON m.subject_id = sub.id
LEFT JOIN students as s ON m.student_id = s.id
WHERE s.id = 1
-- для передачі через консоль розкоментуйте наступний рядок, та закоментуйте попередній
-- WHERE s.id = ?
GROUP BY sub.name; 