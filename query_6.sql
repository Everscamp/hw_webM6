-- Знайти список студентів у певній групі. DONE
SELECT s.name AS studentName, g.name as groupName
FROM groups as g
LEFT JOIN students as s ON s.group_id = g.id
WHERE g.id = 1
-- для передачі через консоль розкоментуйте наступний рядок, та закоментуйте попередній
-- WHERE g.id = ?
GROUP BY s.name ORDER BY g.name; 