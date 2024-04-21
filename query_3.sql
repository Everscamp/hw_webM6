-- Знайти середній бал у групах з певного предмета. DONE
SELECT ROUND(AVG(m.mark), 2) AS avValue, sub.name AS Subject, g.name AS GroupName
FROM marks as m
LEFT JOIN students as s ON m.student_id = s.id
LEFT JOIN subjects as sub ON m.subject_id = sub.id
LEFT JOIN groups as g ON s.group_id = g.id
WHERE s.id = 2 
-- для передачі через консоль розкоментуйте наступний рядок, та закоментуйте попередній
-- WHERE s.id = ?
GROUP BY Subject, g.name
ORDER BY g.name;