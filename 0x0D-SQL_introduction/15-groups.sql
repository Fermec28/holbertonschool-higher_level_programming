-- script that lists the number of records with the same score in the table
SELECT score, COUNT(score) AS average
FROM second_table
GROUP BY score
ORDER BY score DESC;
