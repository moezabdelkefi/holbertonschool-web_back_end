-- Calculate the number of fans for each country origin and rank them
SELECT origin, SUM(fans) AS total_fans
FROM metal_bands
GROUP BY origin
ORDER BY total_fans DESC;
