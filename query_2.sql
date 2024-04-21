-- Знайти студента із найвищим середнім балом з певного предмета. DONE
SELECT MAX(RoundedValue), Subject, Student FROM(SELECT ROUND(AVG(m.mark), 1) AS RoundedValue, sub.name AS Subject, s.name AS Student
FROM marks as m
LEFT JOIN students as s ON m.student_id = s.id
LEFT JOIN subjects as sub ON m.subject_id = sub.id
GROUP BY sub.name,s.name) GROUP BY Subject
ORDER BY RoundedValue DESC;