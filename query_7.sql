-- Знайти оцінки студентів у окремій групі з певного предмета.
SELECT m.mark AS markValue, sub.name AS Subject, g.name AS GroupName, s.name as Student
FROM marks as m
LEFT JOIN students as s ON m.student_id = s.id
LEFT JOIN subjects as sub ON m.subject_id = sub.id
LEFT JOIN groups as g ON s.group_id = g.id
WHERE g.id = 1 AND sub.id = 2; 
-- для передачі через консоль розкоментуйте наступний рядок, та закоментуйте попередній
-- WHERE g.id = ? AND sub.id = ?; 