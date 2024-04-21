-- Оцінки студентів у певній групі з певного предмета на останньому занятті.
SELECT m.mark AS markValue, sub.name AS Subject, g.name AS GroupName, s.name as Student, max(m.fake_date) as fDate
FROM marks as m
LEFT JOIN students as s ON m.student_id = s.id
LEFT JOIN subjects as sub ON m.subject_id = sub.id
LEFT JOIN groups as g ON s.group_id = g.id
WHERE g.id = 2 AND sub.id = 2
-- для передачі через консоль розкоментуйте наступний рядок, та закоментуйте попередній
-- WHERE g.id = ? AND sub.id = ?
GROUP BY s.id; 