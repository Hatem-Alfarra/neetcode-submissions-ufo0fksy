-- Write your query below
SELECT first_name, last_name, address.city, address.state
FROM person LEFT JOIN address ON person.person_id = address.person_id;