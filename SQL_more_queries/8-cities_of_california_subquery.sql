-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT cities.id, cities.name FROM cities, states WHERE states.name = 'California' AND cities.state_id = states.id ORDER BY cities.id;