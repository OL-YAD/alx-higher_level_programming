-- lists all the cities of california that can be found in hbtn_0d_usa
-- 'states' table contains only one record where name = california
--- results must be sorted in ascending order by cities .id
SELECT id, name
FROM cities
WHERE state_id =(
	SELECT id
       	FROM states
	WHERE name = 'California')
	ORDER BY cities.id ASC;
